variable "location" {
  description = "The location for the Cloud Run instance."
  default     = "us-central1"
}

variable "container_image" {
  description = "The container image URL for the Cloud Run service."
}

variable "project_id" {
  description = "The project_id for the specific GCP project."
  default     = "getwib"
}

variable "service_name" {
  description = "The name of the Cloud Run service"
  type        = string
}
