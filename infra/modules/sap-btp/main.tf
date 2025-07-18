provider "btp" {
  globalaccount = var.global_account
  subaccount    = var.subaccount
  region        = var.region
}

resource "btp_subaccount_service_instance" "connector" {
  name            = var.instance_name
  service_name    = "destination"
  service_plan    = "lite"
}

variable "global_account" {}
variable "subaccount" {}
variable "region" { default = "us10" }
variable "instance_name" { default = "sap-btp-connector" }
