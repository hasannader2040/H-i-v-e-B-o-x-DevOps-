provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-east-1" # or your preferred region like "eu-west-1", "me-central-1"
}
