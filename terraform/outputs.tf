output "ingest_url" {
  value = aws_lambda_function_url.ingest_url.function_url
}

output "read_recent_url" {
  value = aws_lambda_function_url.read_url.function_url
}
