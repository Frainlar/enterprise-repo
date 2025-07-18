provider "mongodbatlas" {
  public_key  = var.public_key
  private_key = var.private_key
}

resource "mongodbatlas_project" "project" {
  name   = var.project_name
  org_id = var.org_id
}

resource "mongodbatlas_cluster" "cluster" {
  project_id   = mongodbatlas_project.project.id
  name         = var.cluster_name
  provider_name = "AWS"
  backing_provider_name = "AWS"
  provider_region_name = var.region
}

variable "public_key" {}
variable "private_key" {}
variable "project_name" { default = "enterprise" }
variable "cluster_name" { default = "enterprise" }
variable "org_id" {}
variable "region" { default = "US_EAST_1" }
