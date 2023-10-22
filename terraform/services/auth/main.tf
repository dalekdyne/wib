module "iam" {
  source                = "./modules/iam"
  location              = "us-central1"
  cloudrun_service_name = module.cloudrun.service_name
}

module "cloudrun" {
  source          = "./modules/cloudrun"
  container_image = "us-central1-docker.pkg.dev/${var.project_id}/${var.service_name}/${var.service_name}:latest"
  location        = "us-central1"
  project_id      = var.project_id
  service_name    = var.service_name
}
