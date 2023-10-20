resource "google_storage_bucket" "tf_state_bucket" {
  name     = "tf-states-getwib"
  location = "us-central1"

  // Enable versioning to keep the history of state files
  versioning {
    enabled = true
  }

  storage_class = "STANDARD"
}
