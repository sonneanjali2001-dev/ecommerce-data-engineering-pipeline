-- Run against your Gold fact_sales table after the Spark notebook creates it.
-- Adjust schema/table naming for your Lakehouse SQL endpoint.

-- 1. Net revenue by region/city (exclude cancelled orders)
SELECT shipping_city,
       ROUND(SUM(net_amount), 2) AS net_revenue
FROM fact_sales
WHERE order_status <> 'Cancelled'
GROUP BY shipping_city
ORDER BY net_revenue DESC;

-- 2. Revenue by product category
SELECT category,
       ROUND(SUM(net_amount), 2) AS net_revenue,
       SUM(quantity) AS units_sold
FROM fact_sales
WHERE order_status <> 'Cancelled'
GROUP BY category
ORDER BY net_revenue DESC;

-- 3. Delivery status summary
SELECT order_status,
       COUNT(DISTINCT order_id) AS order_count
FROM fact_sales
GROUP BY order_status
ORDER BY order_count DESC;

-- 4. Customer segment contribution
SELECT customer_segment,
       ROUND(SUM(net_amount), 2) AS net_revenue
FROM fact_sales
WHERE order_status <> 'Cancelled'
GROUP BY customer_segment
ORDER BY net_revenue DESC;
