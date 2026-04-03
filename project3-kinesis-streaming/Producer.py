import boto3
import json
import time
import random
from datetime import datetime

kinesis = boto3.client('kinesis', region_name='us-east-1')

stream_name = 'sales-stream'

regions = ['North', 'South', 'East', 'West']
products = ['Electronics', 'Furniture', 'Clothing', 'Food']
sales_reps = ['Alice', 'Bob', 'Charlie', 'David']

while True:
    data = {
        "sale_id": random.randint(1000, 9999),
        "timestamp": datetime.now().isoformat(),
        "region": random.choice(regions),
        "product_category": random.choice(products),
        "sales_rep": random.choice(sales_reps),
        "sales_amount": round(random.uniform(10, 500), 2)
    }

    kinesis.put_record(
        StreamName=stream_name,
        Data=(json.dumps(data) + "\n"),
        PartitionKey="partitionkey"
    )

    print("Sent:", data)

    time.sleep(2)