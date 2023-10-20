resource "google_service_account" "cloud_run_artifact_sa" {
  account_id   = "cloud-run-artifact-sa"
  display_name = "Service Account for Cloud Run and Artifact Registry"
  description  = "Used for deploying services to Cloud Run and reading/writing to the Artifact Registry"
}

resource "google_service_account_key" "cloud_run_artifact_sa_key" {
  service_account_id = google_service_account.cloud_run_artifact_sa.name
  public_key_type    = "TYPE_X509_PEM_FILE"
}

resource "google_project_iam_binding" "cloud_run_admin" {
  project = var.project_id
  role    = "roles/run.admin"

  members = [
    "serviceAccount:${google_service_account.cloud_run_artifact_sa.email}"
  ]
}

resource "google_project_iam_binding" "service_account_user" {
  project = var.project_id
  role    = "roles/iam.serviceAccountUser"

  members = [
    "serviceAccount:${google_service_account.cloud_run_artifact_sa.email}"
  ]
}

resource "google_project_iam_binding" "artifact_registry_reader" {
  project = var.project_id
  role    = "roles/artifactregistry.reader"

  members = [
    "serviceAccount:${google_service_account.cloud_run_artifact_sa.email}"
  ]
}

resource "google_project_iam_binding" "artifact_registry_writer" {
  project = var.project_id
  role    = "roles/artifactregistry.writer"

  members = [
    "serviceAccount:${google_service_account.cloud_run_artifact_sa.email}"
  ]
}
