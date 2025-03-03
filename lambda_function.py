import boto3
import csv

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
TABLE_NAME = "TaskTable"

def lambda_handler(event, context):
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        object_key = event["Records"][0]["s3"]["object"]["key"]
        
        csv_data = read_csv_from_s3(bucket_name, object_key)
        insert_data_into_dynamodb(csv_data)
        
        return {"status": "Success", "message": "Data inserted into DynamoDB"}
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"status": "Error", "message": str(e)}

def read_csv_from_s3(bucket_name, object_key):
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    lines = response["Body"].read().decode("utf-8").splitlines()
    
    reader = csv.DictReader(lines)
    return [row for row in reader]

def insert_data_into_dynamodb(csv_data):
    table = dynamodb.Table(TABLE_NAME)

    with table.batch_writer() as batch:
        for item in csv_data:
            batch.put_item(Item=item)
    
    print(f"Inserted {len(csv_data)} records into {TABLE_NAME}")
