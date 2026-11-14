# Fabric / PySpark notebook starter
# Update these paths for your own Fabric Lakehouse or Spark environment.
from pyspark.sql import functions as F

# Example local/Lakehouse file paths. In Fabric, upload files to the Lakehouse
# Files area and update these paths accordingly.
BASE_PATH = "Files/ecommerce"
BRONZE_PATH = "Tables/bronze"
SILVER_PATH = "Tables/silver"
GOLD_PATH = "Tables/gold"

customers = spark.read.option("header", True).option("inferSchema", True).csv(f"{BASE_PATH}/customers.csv")
products = spark.read.option("header", True).option("inferSchema", True).csv(f"{BASE_PATH}/products.csv")
orders = spark.read.option("header", True).option("inferSchema", True).csv(f"{BASE_PATH}/orders.csv")
items = spark.read.option("header", True).option("inferSchema", True).csv(f"{BASE_PATH}/order_items.csv")

# Bronze: preserve ingested records and add ingestion timestamp.
for name, df in {
    "customers": customers, "products": products,
    "orders": orders, "order_items": items
}.items():
    (df.withColumn("ingested_at", F.current_timestamp())
       .write.format("delta").mode("overwrite").save(f"{BRONZE_PATH}/{name}"))

# Silver: basic type casting and quality filtering.
customers_s = customers.dropna(subset=["customer_id"]).dropDuplicates(["customer_id"])
products_s = (products.dropna(subset=["product_id"])
              .dropDuplicates(["product_id"])
              .withColumn("unit_price", F.col("unit_price").cast("double")))
orders_s = (orders.dropna(subset=["order_id", "customer_id"])
            .dropDuplicates(["order_id"])
            .withColumn("order_date", F.to_date("order_date")))
items_s = (items.dropna(subset=["order_id", "product_id"])
           .withColumn("quantity", F.col("quantity").cast("int"))
           .withColumn("unit_price", F.col("unit_price").cast("double"))
           .withColumn("discount_pct", F.col("discount_pct").cast("double"))
           .filter((F.col("quantity") > 0) & (F.col("unit_price") >= 0))
           .dropDuplicates(["order_id", "product_id"]))

silver_tables = {
    "customers": customers_s, "products": products_s,
    "orders": orders_s, "order_items": items_s
}
for name, df in silver_tables.items():
    df.write.format("delta").mode("overwrite").save(f"{SILVER_PATH}/{name}")

# Gold: order-line sales fact enriched with customer and product attributes.
gold = (items_s.join(orders_s, "order_id", "inner")
        .join(customers_s, "customer_id", "left")
        .join(products_s, "product_id", "left")
        .withColumn("gross_amount", F.col("quantity") * F.col("unit_price"))
        .withColumn("discount_amount", F.col("gross_amount") * F.col("discount_pct"))
        .withColumn("net_amount", F.col("gross_amount") - F.col("discount_amount"))
        .select("order_id", "order_date", "order_status", "customer_id",
                "customer_segment", "shipping_city", "product_id",
                "product_name", "category", "quantity", "gross_amount",
                "discount_amount", "net_amount"))
gold.write.format("delta").mode("overwrite").save(f"{GOLD_PATH}/fact_sales")

# Simple validation output
print("Gold row count:", gold.count())
gold.groupBy("order_status").agg(F.countDistinct("order_id").alias("orders")).show()
