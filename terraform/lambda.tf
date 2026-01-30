resource "aws_lambda_function" "ingest" {
  function_name = "log_ingest"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.11"
  handler       = "handler.handler"
  filename      = "../lambdas/ingest/handler.zip"

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.logs.name
    }
  }
}

resource "aws_lambda_function" "read_recent" {
  function_name = "log_read_recent"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.11"
  handler       = "handler.handler"
  filename      = "../lambdas/read_recent/handler.zip"

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.logs.name
    }
  }
}

resource "aws_lambda_function_url" "ingest_url" {
  function_name      = aws_lambda_function.ingest.function_name
  authorization_type = "AWS_IAM"
}

resource "aws_lambda_function_url" "read_url" {
  function_name      = aws_lambda_function.read_recent.function_name
  authorization_type = "AWS_IAM"
}
