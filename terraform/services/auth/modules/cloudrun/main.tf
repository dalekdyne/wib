resource "google_cloud_run_service" "getwib_auth" {
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
