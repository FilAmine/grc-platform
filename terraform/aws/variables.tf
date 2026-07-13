variable "aws_region" {
  description = "AWS region to deploy into."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Prefix applied to every resource name and tag."
  type        = string
  default     = "grc-platform"
}

variable "environment" {
  description = "Deployment environment name (e.g. staging, production). Affects resource naming and RDS/ElastiCache sizing defaults below."
  type        = string
  default     = "production"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC this module creates. Change if it collides with existing VPCs you peer/connect to."
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zone_count" {
  description = "Number of AZs to spread subnets across."
  type        = number
  default     = 3
}

variable "eks_cluster_version" {
  description = "Kubernetes version for the EKS control plane. Pin explicitly; AWS deprecates old versions on a schedule."
  type        = string
  default     = "1.29"
}

variable "eks_node_instance_types" {
  description = "Instance types for the EKS managed node group."
  type        = list(string)
  default     = ["t3.medium"]
}

variable "eks_node_min_size" {
  type    = number
  default = 2
}

variable "eks_node_max_size" {
  type    = number
  default = 5
}

variable "eks_node_desired_size" {
  type    = number
  default = 2
}

variable "rds_instance_class" {
  description = "RDS instance class for Postgres. db.t3.micro is free-tier-eligible but not sized for real production load -- bump before using this for anything real."
  type        = string
  default     = "db.t3.micro"
}

variable "rds_allocated_storage_gb" {
  type    = number
  default = 20
}

variable "rds_engine_version" {
  description = "Postgres major version. Match backend/Dockerfile's psycopg driver compatibility (currently tested against Postgres 16 in CI -- see .github/workflows/ci.yml)."
  type        = string
  default     = "16"
}

variable "rds_database_name" {
  type    = string
  default = "grc_platform"
}

variable "rds_master_username" {
  type    = string
  default = "grc"
}

variable "rds_master_password" {
  description = "REQUIRED, no default on purpose -- pass via -var, a .tfvars file excluded from version control, or (better) TF_VAR_rds_master_password so it never touches disk in plaintext. This module does not create a Secrets Manager entry for it; see this directory's README for why that's a deliberate scope cut, not an oversight."
  type        = string
  sensitive   = true
}

variable "redis_node_type" {
  description = "ElastiCache node type. cache.t3.micro is the smallest available -- bump before using this for anything real."
  type        = string
  default     = "cache.t3.micro"
}

variable "tags" {
  description = "Extra tags merged onto every resource this module creates."
  type        = map(string)
  default     = {}
}
