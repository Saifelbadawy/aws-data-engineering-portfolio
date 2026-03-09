 AWS Sales Data Lake Project

## Project Overview
This project demonstrates how to build a simple data lake using AWS services.

## Architecture
The project uses:
- Amazon S3 for storing raw data
- AWS Glue Crawler for schema detection
- AWS Glue Data Catalog for table metadata
- Amazon Athena for querying the data using SQL

## Steps Implemented
1. Uploaded sales data to S3
2. Created a Glue Crawler
3. Generated a table in Glue Data Catalog
4. Queried the data using Athena

## Example Query
```sql
SELECT *
FROM sales_data
LIMIT 10;
````

## Technologies Used

* AWS S3
* AWS Glue
* AWS Athena
* SQL




