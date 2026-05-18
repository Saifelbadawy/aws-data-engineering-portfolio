&#x20;EC2 Automated Weather Data Pipeline



A production-style data engineering pipeline deployed on AWS EC2. The pipeline

automatically collects weather data from a public API on an hourly schedule,

transforms it into a columnar format, stores it in a partitioned S3 data lake,

and makes it queryable with SQL via Amazon Athena.



\## Architecture



Open-Meteo API → EC2 (Python + Cron) → S3 (Parquet, partitioned) → Athena (SQL)



\## Tech Stack



| Service | Role |

|---------|------|

| AWS EC2 (t2.micro) | Pipeline compute — runs Python ETL on a cron schedule |

| Amazon S3 | Data lake — stores Parquet files, partitioned by date |

| Amazon Athena | Serverless SQL queries directly on S3 data |

| AWS IAM | EC2 role-based access to S3 (no hardcoded keys) |

| Python / boto3 | ETL logic, API calls, S3 uploads |

| Apache Parquet | Columnar storage format for efficient querying |



\## Key Features



\- Scheduled hourly ingestion via cron (no manual intervention)

\- Multi-city weather tracking (Cairo, London, New York, Tokyo)

\- Data transformation and enrichment before storage

\- Hive-style S3 partitioning (year=/ month=/ day=/) for Athena performance

\- Snappy-compressed Parquet reduces Athena scan cost by \~80% vs CSV

\- IAM role-based auth — zero hardcoded credentials

\- Structured logging to file and stdout



\## Data Flow



1\. Cron triggers `pipeline.py` every hour

2\. Script calls Open-Meteo REST API for 4 cities

3\. Transforms JSON responses into flat records

4\. Writes a Parquet file to S3 with date partitioning

5\. Athena external table reads from S3 on demand



\## Setup \& Deployment



\### Prerequisites

\- AWS account with EC2 + S3 + Athena access

\- IAM role with S3 write permissions attached to EC2



\### Installation

```bash

git clone https://github.com/yourusername/ec2-weather-data-pipeline.git

cd ec2-weather-data-pipeline



\# On EC2 instance

pip3 install -r requirements.txt



\# Edit S3\_BUCKET in src/pipeline.py

\# Run once to test

python3 src/pipeline.py



\# Schedule hourly runs

crontab -e

\# Add: 0 \* \* \* \* /usr/bin/python3 /home/ec2-user/weather-pipeline/src/pipeline.py

```



\## Sample Athena Queries



```sql

\-- Latest readings across all cities

SELECT city, temperature\_c, humidity\_pct, ingestion\_timestamp

FROM weather\_db.weather\_readings

ORDER BY ingestion\_timestamp DESC LIMIT 20;



\-- Average temperature by city

SELECT city, ROUND(AVG(temperature\_c), 2) AS avg\_temp\_c

FROM weather\_db.weather\_readings

GROUP BY city ORDER BY avg\_temp\_c DESC;

```



\## Cost



This project runs within the AWS Free Tier (12 months):

\- EC2 t2.micro: 750 hrs/month free

\- S3: <5 MB data, well within 5 GB free tier

\- Athena: \~$0.00 (Parquet + Snappy = minimal scan size)



