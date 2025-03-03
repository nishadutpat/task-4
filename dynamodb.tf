resource "aws_dynamodb_table" "task_table" {
  name         = "TaskTable"
  

  hash_key = "id"

  attribute {
    name = "id"
    type = "S"
  }
}