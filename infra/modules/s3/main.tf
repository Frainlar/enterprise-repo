provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "bucket" {
  bucket = var.bucket_name
}

variable "aws_region" {
  default = "us-east-1"
}
variable "bucket_name" {
  description = "Name of the bucket"
}
