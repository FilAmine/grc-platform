# Uses the community terraform-aws-modules/vpc and terraform-aws-modules/eks
# registry modules rather than hand-rolled aws_vpc/aws_eks_cluster resource
# blocks -- these are the de facto standard way to provision a VPC/EKS
# cluster with Terraform (widely used, actively maintained), and leaning on
# them here keeps this module's own surface area smaller and less prone to
# the kind of subtle networking/IAM mistakes that are easy to make
# hand-rolling EKS from scratch. Still entirely unverified -- see this
# directory's README.

locals {
  name = "${var.project_name}-${var.environment}"
  tags = merge(
    {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "terraform"
    },
    var.tags,
  )
}

data "aws_availability_zones" "available" {
  state = "available"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = local.name
  cidr = var.vpc_cidr

  azs             = slice(data.aws_availability_zones.available.names, 0, var.availability_zone_count)
  private_subnets = [for i in range(var.availability_zone_count) : cidrsubnet(var.vpc_cidr, 4, i)]
  public_subnets  = [for i in range(var.availability_zone_count) : cidrsubnet(var.vpc_cidr, 4, i + var.availability_zone_count)]

  enable_nat_gateway   = true
  single_nat_gateway   = var.environment != "production" # one shared NAT for non-prod to cut cost; one-per-AZ for prod HA
  enable_dns_hostnames = true

  # Required tags for the EKS/ELB controllers to auto-discover subnets.
  public_subnet_tags = {
    "kubernetes.io/role/elb" = "1"
  }
  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = "1"
  }

  tags = local.tags
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = local.name
  cluster_version = var.eks_cluster_version

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  # Public API endpoint for simplicity (kubectl/CI access without a VPN/bastion).
  # Restrict cluster_endpoint_public_access_cidrs before using this for anything
  # real -- open to 0.0.0.0/0 by this module's own default otherwise.
  cluster_endpoint_public_access = true

  eks_managed_node_groups = {
    default = {
      instance_types = var.eks_node_instance_types
      min_size       = var.eks_node_min_size
      max_size       = var.eks_node_max_size
      desired_size   = var.eks_node_desired_size
    }
  }

  tags = local.tags
}
