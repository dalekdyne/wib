terraform {
  backend "gcs" {
    bucket = "tf-states-getwib"
    prefix = "auth"
  }
}
