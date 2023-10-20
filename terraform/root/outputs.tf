output "bucket_url" {
  description = "The URL of the created storage bucket."
  value       = "gs://${google_storage_bucket.tf_state_bucket.name}"
}
