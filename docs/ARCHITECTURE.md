# E-Commerce Data Engineering Architecture

## 1. Project Architecture

This project follows a Medallion Architecture to process e-commerce data through multiple layers.

## 2. Data Flow

```text
   Source CSV Files
          |
          v
   Azure Data Factory
          |
          v
   Azure Data Lake Storage Gen2
          |
          v
     Landing Layer
          |
          v
     Bronze Layer
    (Raw Data Storage)
          |
          v
     Silver Layer
 (Cleaning & Transformation)
          |
          v
      Gold Layer
 (Business-Ready Data)
          |
          v
   Microsoft Fabric Lakehouse
          |
          v
     SQL Analytics
          |
          v
       Power BI
```

## 3. Architecture Components

### Landing Layer
Stores incoming raw e-commerce source files.

### Bronze Layer
Maintains ingested data in Delta format.

### Silver Layer
Performs data cleaning, validation and transformation using PySpark.

### Gold Layer
Contains business-ready datasets for analytical reporting.

## 4. Business Insights

- Regional sales performance
- Customer segmentation
- Order and delivery analysis
- Revenue and discount analysis
- Delivery SLA monitoring

## 5. Technologies

Azure Data Factory | ADLS Gen2 | PySpark | Delta Lake | Microsoft Fabric | SQL | Power BI

---

**Project:** E-Commerce Data Engineering Pipeline  
**Author:** Anjali Sonni
