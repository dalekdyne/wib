resource "google_cloud_run_service" "getwib_api" {
  name     = var.service_name
  location = var.location

  traffic {
    percent         = 100
    latest_revision = true
  }

  template {
    spec {
      containers {
        image = var.container_image
        env {
          name  = "DATABASE_URL"
          value = "test"
        }
      }
    }
    # metadata {
    #   annotations = {
    #     "run.googleapis.com/cloudsql-instances" = data.google_sql_database_instance.getwib_api.connection_name
    #   }
    # }
  }
}


resource "google_cloud_run_domain_mapping" "getwib_api_domain_mapping" {
  location = var.location
  name     = "api.getwib.com"

  metadata {
    namespace = var.project_id
  }

  spec {
    route_name = google_cloud_run_service.getwib_api.name
  }
}
