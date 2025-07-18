provider "aws" {
  region = var.aws_region
}

resource "aws_athena_workgroup" "wg" {
  name = var.workgroup_name
  state = "ENABLED"
}

variable "aws_region" {
  default = "us-east-1"
}
variable "workgroup_name" {
  default = "enterprise"
}
