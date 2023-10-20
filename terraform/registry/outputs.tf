output "repository_urls" {
  value = [
    for repo in google_artifact_registry_repository.artifact_repositories : 
    "us-central1-docker.pkg.dev/${var.project_id}/${repo.repository_id}"
  ]
  description = "URLs of the created artifact repositories"
}
