provider "aws" {
  region = var.aws_region
}

resource "aws_glue_catalog_database" "datalake" {
  name = "enterprise_datalake"
  description = "Glue database for S3-based data lake"
}

resource "aws_glue_catalog_table" "agent_log" {
  name          = "agent_log"
  database_name = aws_glue_catalog_database.datalake.name
  table_type    = "EXTERNAL_TABLE"

  parameters = {
    classification = "parquet"
  }

  storage_descriptor {
    location      = "s3://enterprise-datalake/agent_log/"
    input_format  = "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat"
    output_format = "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat"

    serde_info {
      serialization_library = "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
    }
  }
}

variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}
