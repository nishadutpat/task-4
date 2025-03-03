resource "aws_lambda_function" "csv_lambda" {
  function_name    = "CSVToDynamoDB"
  role            = aws_iam_role.lambda_role.arn  # Ensure the role is declared before this
  handler         = "lambda_function.lambda_handler"
  runtime         = "python3.9"
  timeout         = 30

  filename         = "lambda_function.zip"
  source_code_hash = filebase64sha256("lambda_function.zip")
}
