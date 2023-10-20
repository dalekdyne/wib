resource "google_artifact_registry_repository" "artifact_repositories" {
  for_each = toset(var.repositories)

  location      = var.location
  repository_id = each.value
  format        = "DOCKER"

  description = "Docker repository for ${each.value}"
}
