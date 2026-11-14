# Architecture

```text
CSV source files
      |
      v
Azure Data Factory (copy/orchestration)
      |
      v
ADLS Gen2 - Landing
      |
      v
Bronze Delta (raw ingested data)
      |
      v
Silver Delta (cleaned and validated data)
      |
      v
Gold Delta (business-ready sales model)
      |
      v
SQL analytics / Power BI
```

## Layer responsibilities
- **Landing:** immutable source-file drop zone.
- **Bronze:** source-aligned data with ingestion metadata.
- **Silver:** standardized types, validated keys, filtered invalid rows.
- **Gold:** joined sales fact and dimensions for reporting.

This is a conceptual architecture for the learning project. Add an actual architecture screenshot after implementing it in your cloud workspace.
