resource "google_cloud_run_service_iam_member" "public_access" {
  service  = var.cloudrun_service_name
  location = var.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}
