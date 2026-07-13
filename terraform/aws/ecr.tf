# Container registries for the two images this repo builds --
# backend/Dockerfile and frontend/Dockerfile. Push here instead of the
# generic ghcr.io/your-org/... placeholders k8s/ and helm/ reference by
# default; update those values (k8s/*.yaml's image: fields, or
# helm/grc-platform/values.yaml's backend.image.repository/
# frontend.image.repository) to point at these repository URLs once created.

resource "aws_ecr_repository" "backend" {
  name                 = "${var.project_name}-backend"
  image_tag_mutability = "IMMUTABLE" # forces real tags (git SHA, semver) over floating `latest`

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = local.tags
}

resource "aws_ecr_repository" "frontend" {
  name                 = "${var.project_name}-frontend"
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = local.tags
}
