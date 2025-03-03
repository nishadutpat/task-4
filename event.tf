
resource "aws_s3_bucket_notification" "s3_trigger" {
  bucket = aws_s3_bucket.buck-for-task-4.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.csv_lambda.arn
    events              = ["s3:ObjectCreated:*"]
    filter_suffix       = ".csv"
  }
}
