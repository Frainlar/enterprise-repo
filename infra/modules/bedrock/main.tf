provider "aws" {
  region = var.aws_region
}

resource "aws_bedrock_agent" "this" {
  name             = var.agent_name
  foundation_model = var.model_id
}

variable "aws_region" {
  default = "us-east-1"
}
variable "agent_name" {
  default = "bedrock-agent"
}
variable "model_id" {
  default = "anthropic.claude-v2"
}
