variable "project_id" {
  description = "The ID of the project in which resources will be managed."
  type        = string
  default     = "getwib"
}

variable "service_name" {
  description = "The name of the service being deployed in cloudrun"
  type        = string
  default     = "getwib-meeting"
}
