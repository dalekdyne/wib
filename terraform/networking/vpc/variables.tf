variable "project_id" {
  description = "The ID of the project in which resources will be provisioned."
  type        = string
  default     = "getwib"
}

variable "vpc_name" {
  description = "The name of the VPC."
  type        = string
}

variable "subnets" {
  description = "A map of subnets to create within the VPC."
  type = map(object({
    region        = string
    ip_cidr_range = string
  }))
}
