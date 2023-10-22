variable "project_id" {
  description = "The ID of the GCP project."
  type        = string
}

variable "vpc_name" {
  description = "The name of the VPC."
  type        = string
}

variable "api_name" {
  description = "The name of the API."
  type        = string
}

variable "api_config_name" {
  description = "The name of the API configuration."
  type        = string
}

variable "gateway_name" {
  description = "The name of the gateway."
  type        = string
}

variable "cloud_run_service" {
  description = "Map of Cloud Run services URLs."
  type        = map(string)
}
