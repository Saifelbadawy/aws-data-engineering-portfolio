\# AWS Glue ETL Pipeline (Project 2)



\## Overview

This project implements an ETL pipeline using AWS Glue to transform raw CSV sales data stored in Amazon S3 into an optimized Parquet dataset for analytics.



\## Architecture

S3 (raw data) → AWS Glue ETL → S3 (processed Parquet) → Glue Data Catalog → Athena



\## Technologies Used

\- Amazon S3

\- AWS Glue (ETL jobs)

\- AWS Glue Data Catalog

\- Amazon Athena

\- SQL



\## Dataset

Sales dataset containing:

\- product\_id

\- sale\_date

\- sales\_rep

\- region

\- sales\_amount

\- quantity\_sold

\- product\_category

\- unit\_cost

\- unit\_price

\- discount

\- payment\_method



\## Transformations

\- Removed redundant column: region\_and\_sales\_rep

\- Created new columns:

&#x20; - total\_cost = unit\_cost × quantity\_sold

&#x20; - total\_profit = sales\_amount − total\_cost

\- Converted CSV data to Parquet format



\## Output

Processed dataset stored in:

s3://<your-bucket>/processed/sales\_parquet/



\## Example Queries



\### Revenue by Region

```sql

SELECT region, SUM(sales\_amount) AS revenue

FROM sales\_processed\_parquet

GROUP BY region;

