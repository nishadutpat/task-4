resource "aws_dynamodb_table" "task_table" {
  name         = "Task_table"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "id"

  attribute {
    name = "id"
    type = "S"
  }
}