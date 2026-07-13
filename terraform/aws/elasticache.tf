# Managed Redis -- backs both rate limiting (backend/app/core/rate_limit.py)
# and the Celery broker/result backend (backend/app/core/celery_app.py).
# A single cache.t3.micro node, not a replication group -- both call sites
# already fail open / retry on a missing Redis (see rate_limit.py's
# docstring), so this is a real but accepted tradeoff, matching the
# k8s/Helm chart's single-replica Redis StatefulSet.

resource "aws_elasticache_subnet_group" "redis" {
  name       = "${local.name}-redis"
  subnet_ids = module.vpc.private_subnets
  tags       = local.tags
}

resource "aws_security_group" "redis" {
  name_prefix = "${local.name}-redis-"
  description = "Allow Redis access from the EKS node security group only."
  vpc_id      = module.vpc.vpc_id

  ingress {
    description     = "Redis from EKS nodes"
    from_port       = 6379
    to_port         = 6379
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

resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "${local.name}-redis"
  engine               = "redis"
  node_type            = var.redis_node_type
  num_cache_nodes      = 1
  port                 = 6379
  subnet_group_name    = aws_elasticache_subnet_group.redis.name
  security_group_ids   = [aws_security_group.redis.id]
  apply_immediately    = var.environment != "production"

  tags = local.tags
}
