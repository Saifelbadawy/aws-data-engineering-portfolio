\# 🚀 Serverless Data Processing Pipeline using AWS Lambda



\## 📌 Overview

This project demonstrates a serverless data engineering pipeline built on AWS. The system automatically processes incoming CSV files using AWS Lambda triggered by Amazon S3 events. Cleaned data is stored in a processed layer and made available for querying using Amazon Athena.



\---



\## 🧱 Architecture

S3 (raw) → Lambda → S3 (processed) 



\---



\## ⚙️ Technologies Used

\- Amazon S3  

\- AWS Lambda  

&#x20;

\- Python (boto3)



\---



&#x20;Workflow

1\. Upload a raw CSV file to the `raw/` folder in S3  

2\. S3 triggers the Lambda function automatically  

3\. Lambda processes the file:

&#x20;  - Removes rows with missing values  

&#x20;  - Standardizes text fields (e.g., uppercase)  

4\. Cleaned data is saved in the `processed/` folder  



\---



&#x20;Sample Data



\### Input (raw data)

```csv

sale\_id,product,amount

1,phone,500

2,laptop,1200

3,,300

4,tablet,

5,phone,500

