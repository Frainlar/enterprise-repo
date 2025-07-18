provider "aws" {
  region = var.aws_region
}

resource "aws_glue_catalog_database" "db" {
  name = var.database_name
}

variable "aws_region" {
  default = "us-east-1"
}
variable "database_name" {
  default = "enterprise_datalake"
}
