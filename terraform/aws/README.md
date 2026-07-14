# Terraform (AWS)

Provisions the cloud infrastructure `helm/`'s Helm chart (or `k8s/`'s plain
manifests) needs to run somewhere real: a VPC, an EKS cluster, managed
Postgres (RDS) and Redis (ElastiCache), and two ECR repositories for the
backend/frontend images.

## Status: init + validate clean, no real AWS account exercised

Unlike `k8s/` and `helm/` — which only needed *a* Kubernetes cluster,
generically — Terraform inherently means committing to a specific cloud
provider and account-level decisions (region, network layout, instance
sizing) that only make sense in the context of a real account. Nothing in
this repo previously specified a cloud provider, so **AWS was chosen here
as the most common default**, not because it's stated anywhere else in the
codebase. If your actual target is GCP, Azure, or on-prem, this module
isn't directly useful beyond illustrating the shape of what's needed
(VPC/cluster/managed DB/managed cache/image registries).

Updated: `terraform` is now installed (via `winget`), which allowed real
checks beyond the original "no terraform binary available" state:

- `terraform init` resolves and downloads the `hashicorp/aws` provider
  (v5.100.0) and both `terraform-aws-modules/vpc`/`terraform-aws-modules/eks`
  registry modules (plus their transitive `kms`/fargate-profile/node-group
  submodules) with no errors — confirms every module source/version
  constraint in `main.tf` is valid and resolvable. `.terraform.lock.hcl`,
  the resulting provider version lock file, is now committed per
  Terraform's own recommended practice.
- `terraform validate` passes clean — confirms every resource block,
  variable type, and reference across all 7 `.tf` files is syntactically
  correct and matches the AWS provider's actual resource schemas (not
  just "looks like HCL," genuine schema-level validation).
- `terraform plan` was also attempted, and fails **exactly** where
  expected — `Error: No valid credential sources found` — confirming the
  failure boundary is "needs real AWS credentials," not a hidden config
  bug. No AWS account, credentials, or real cloud resources were used or
  created; nothing here has been `apply`d.

**No cost was incurred and no real infrastructure was created or
touched.** Treat this as a starting scaffold that needs a real AWS
account, real `terraform plan` review against that account's actual
state, and probably some adjustment (instance sizing, the public EKS
endpoint default, backup/retention policy) before it's applied anywhere —
schema-valid HCL is a real, meaningful bar cleared, but it's not the same
as "this will provision correctly" (e.g. IAM permission requirements for
the executing principal, real AZ availability in your chosen region,
service quotas). Leans on the community `terraform-aws-modules/vpc` and
`terraform-aws-modules/eks` registry modules rather than hand-rolled
resource blocks specifically to reduce that risk — they're the de facto
standard way to provision this, not a novel design.

## What this provisions

- A VPC (public + private subnets across `availability_zone_count` AZs,
  one NAT gateway per AZ in `production`, a single shared one otherwise).
- An EKS cluster with one managed node group.
- An RDS Postgres instance (private subnets only, security group scoped
  to the EKS node security group — not publicly reachable).
- An ElastiCache Redis node (same private/security-group-scoped pattern).
- Two ECR repositories (`image_tag_mutability = "IMMUTABLE"`, forcing real
  tags instead of a floating `latest`).

## What's deliberately not here

- **A real secrets management setup.** `rds_master_password` is a plain
  Terraform variable (`sensitive = true` only suppresses it from CLI
  output/state diffs shown to the user — the value is still stored
  plaintext in Terraform state). A real setup would generate it with
  `random_password`, store it in AWS Secrets Manager, and have the backend
  pull it at runtime (e.g. via the Secrets Store CSI driver) — a
  genuinely separate piece of work, matching this repo's existing
  `k8s/secret.example.yaml` stopgap for the same underlying gap.
- **Terraform remote state / backend configuration** (S3 + DynamoDB
  locking, or Terraform Cloud) — this module as written uses local state,
  fine for a first `plan` review, not for real collaborative use.
- WAF, GuardDuty, multi-region/DR, VPC peering, a bastion host or VPN for
  private cluster-endpoint access (the EKS endpoint is public by default
  here, restrict `cluster_endpoint_public_access_cidrs` before using this
  for anything real), and CI/CD wiring to actually run `terraform apply`
  (this repo's `.github/workflows/ci.yml` doesn't touch this directory at
  all).

## Apply sequence (once you have a real AWS account and reviewed the plan)

```bash
cd terraform/aws
terraform init
terraform plan -var="rds_master_password=<a real password>"
terraform apply -var="rds_master_password=<a real password>"

# Point kubectl at the new cluster:
terraform output -raw eks_kubeconfig_command | bash

# Then push images to the ECR repos this created and follow
# helm/README.md's or k8s/README.md's install sequence, updating the
# image repository values to the ecr_*_repository_url outputs.
```
