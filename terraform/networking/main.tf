module "vpc" {
  source = "./vpc"

  project_id = var.project_id
  vpc_name   = "getwib-vpc"
  subnets = {
    subnet-a = {
      region        = "us-central1"
      ip_cidr_range = "10.0.0.0/20"
    }
    subnet-b = {
      region        = "us-west1"
      ip_cidr_range = "10.0.16.0/20"
    }
  }
}

# module "loadbalancer" {
#   source = "./loadbalancer"
# }