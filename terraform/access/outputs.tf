output "service_account_email" {
  description = "The email of the created service account."
  value       = google_service_account.cloud_run_artifact_sa.email
}

output "service_account_json_key" {
  description = "The JSON key of the created service account. Handle with care!"
  value       = google_service_account_key.cloud_run_artifact_sa_key.private_key
  sensitive   = true
}
