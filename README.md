# E-Commerce Data Engineering Pipeline

A portfolio-ready **learning/demo project** showing how e-commerce source files can be ingested, cleaned, modelled, and prepared for analytics using a Medallion-style design.

> **Important:** This repository contains synthetic sample data and starter code/templates. It is not evidence of a deployed Azure/Fabric environment. Replace the sample configuration with your own resource details and run/test each component before describing it as production experience.

## Technology mapping
- Azure Data Factory (ADF): orchestration and copy activity template (`pipelines/`)
- Azure Data Lake Storage Gen2: landing/raw storage target (configure your own storage account)
- Microsoft Fabric Lakehouse / Spark: notebook starter (`notebooks/`)
- PySpark + Delta Lake: Bronze, Silver and Gold transformations
- SQL: analytical queries (`sql/`)
- Power BI: connect to the Gold output after running the pipeline

## Repository structure
```text
data/        Synthetic CSV source files
notebooks/   PySpark notebook starter
sql/         SQL transformations and KPI queries
pipelines/   Parameterized ADF pipeline example
docs/        Architecture and run instructions
screenshots/ 
```

## Data flow
1. Copy the four CSV source files to a landing folder in ADLS Gen2.
2. Ingest the files into Bronze Delta tables.
3. Clean and validate records into Silver tables.
4. Join orders, order items, customers and products into Gold sales facts.
5. Query Gold tables for sales, customer, category and delivery insights.

## Quick start
See [`docs/SETUP.md`](docs/SETUP.md). The sample CSVs are intentionally small and synthetic so you can practise safely.

## Author
Anjali Sonni
