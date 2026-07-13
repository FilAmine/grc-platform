# Managed Postgres -- matches docs/deployment.md's standing recommendation
# to point DATABASE_URL at a managed, backed-up instance rather than the
# k8s/Helm chart's in-cluster StatefulSet fallback.

resource "aws_db_subnet_group" "postgres" {
  name       = "${local.name}-postgres"
  subnet_ids = module.vpc.private_subnets
  tags       = local.tags
}

resource "aws_security_group" "postgres" {
  name_prefix = "${local.name}-postgres-"
  description = "Allow Postgres access from the EKS node security group only."
  vpc_id      = module.vpc.vpc_id

  ingress {
    description     = "Postgres from EKS nodes"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [module.eks.node_security_group_id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = local.tags

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_db_instance" "postgres" {
  identifier     = "${local.name}-postgres"
  engine         = "postgres"
  engine_version = var.rds_engine_version

  instance_class    = var.rds_instance_class
  allocated_storage = var.rds_allocated_storage_gb
  storage_encrypted = true

  db_name  = var.rds_database_name
  username = var.rds_master_username
  password = var.rds_master_password

  db_subnet_group_name   = aws_db_subnet_group.postgres.name
  vpc_security_group_ids = [aws_security_group.postgres.id]
  publicly_accessible    = false

  backup_retention_period = var.environment == "production" ? 7 : 1
  skip_final_snapshot     = var.environment != "production"
  deletion_protection     = var.environment == "production"

  tags = local.tags
}
