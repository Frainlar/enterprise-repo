provider "aws" {
  region = var.aws_region
}

resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "enterprise-redis"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
}

variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}
