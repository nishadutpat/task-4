resource "aws_dynamodb_table" "task4_table" {
  name         = "Task4_table"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "id"

  attribute {
    name = "id"
    type = "S"
  }
}