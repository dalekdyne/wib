variable "location" {
  description = "The location of the artifact repository"
  type        = string
  default     = "us-central1"
}

variable "repositories" {
  description = "List of repository names to create"
  type        = list(string)
  default     = [
    "getwib-api",
    "getwib-auth",
    "getwib-mailing",
    "getwib-meeting",
    "getwib-studio",
    "getwib-user"
  ]
}

variable "project_id" {
  description = "The ID of the project in which resources will be managed."
  type        = string
  default     = "getwib"
}
