import boto3
import csv
import urllib.parse

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
TABLE_NAME = "Task4_table"

def lambda_handler(event, context):
    try:
        # Extract S3 bucket name and file key from the event
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        object_key = event["Records"][0]["s3"]["object"]["key"]
        object_key = urllib.parse.unquote_plus(object_key)  # Decode URL-encoded key

        print(f"Reading file {object_key} from bucket {bucket_name}")

        # Read CSV from S3
        csv_data = read_csv_from_s3(bucket_name, object_key)

        # Insert data into DynamoDB
        insert_data_into_dynamodb(csv_data)

        return {"status": "Success", "message": "Data inserted into DynamoDB"}
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"status": "Error", "message": str(e)}

def read_csv_from_s3(bucket_name, object_key):
    """Reads a CSV file from S3 and returns a list of dictionaries."""
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)  # FIXED
    lines = response["Body"].read().decode("utf-8").splitlines()

    reader = csv.DictReader(lines)
    return [row for row in reader]

def insert_data_into_dynamodb(csv_data):
    """Inserts CSV data into a DynamoDB table using batch writing."""
    table = dynamodb.Table(TABLE_NAME)

    with table.batch_writer() as batch:
        for item in csv_data:
            batch.put_item(Item=item)

    print(f"Inserted {len(csv_data)} records into {TABLE_NAME}")
