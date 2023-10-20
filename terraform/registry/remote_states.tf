terraform {
  backend "gcs" {
    bucket = "tf-states-getwib"
    prefix = "artifact_registry"
  }
}
