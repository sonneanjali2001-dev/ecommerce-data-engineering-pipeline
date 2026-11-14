# Setup and execution guide

## 1. Inspect the sample data
The `data/` directory contains synthetic customers, products, orders and order_items CSV files. They are demonstration records, not real customer data.

## 2. Create cloud resources (when ready)
Create an Azure Storage account with hierarchical namespace enabled, an ADLS Gen2 container, and a Microsoft Fabric workspace with a Lakehouse. Do not publish credentials, keys, SAS tokens, or connection strings in GitHub.

## 3. Landing / ingestion
Upload the CSV files to a landing path such as:
`abfss://<container>@<storage-account>.dfs.core.windows.net/landing/<entity>/`

Configure ADF linked services and datasets using your own secure connection settings. `pipelines/adf_copy_pipeline_template.json` is an illustrative template; it must be adapted and validated in ADF before use.

## 4. Run the Spark notebook
Open `notebooks/ecommerce_medallion_pipeline.py` in a Fabric notebook (or adapt it to your Spark environment). Update the input and output paths. The notebook demonstrates CSV ingestion, basic data quality checks, Delta writes and Gold joins.

## 5. Run SQL
Use `sql/gold_kpi_queries.sql` against the Gold tables after creating them. Table names and paths may need adjustment for your Lakehouse SQL endpoint.

## 6. Validate and document
Check row counts, nulls, duplicate keys, order statuses and revenue totals. Save your own screenshots in `screenshots/` only after you have run the pipeline. Record any changes you make.

## Portfolio honesty
Until you have executed and validated the components in your own environment, describe this as a project you are building or a hands-on demo. Do not claim cloud deployment, scale, performance improvements, or production usage that you have not measured.
