module "vpc" {
  source = "./modules/vpc"

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

module "api_gateway" {
  source = "./modules/gateway"

  project_id     = var.project_id
  vpc_name       = var.vpc_name
  api_name       = var.api_name
  api_config_name= var.api_config_name
  gateway_name   = var.gateway_name
  cloud_run_service = {
    service_1 = "service-1-url",
    service_2 = "service-2-url"
    // Add more services as needed
  }
}