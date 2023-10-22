
resource "google_apigateway_api" "api" {
  provider = google

  api_id = var.api_name
  project = var.project_id
  location = "us-central1"
}

resource "google_apigateway_api_config" "config" {
  provider = google

  api_config_id = var.api_config_name
  api = google_apigateway_api.api.api_id
  project = var.project_id
  location = "us-central1"

  # Assuming openapi spec file is in the same directory.
  # Modify this as per your openapi spec file's location.
  openapi_documents {
    document {
      path = "openapi-spec.yaml"
      contents = filebase64("openapi-spec.yaml")
    }
  }
}

resource "google_apigateway_gateway" "gateway" {
  provider = google

  gateway_id = var.gateway_name
  api = google_apigateway_api.api.api_id
  api_config = google_apigateway_api_config.config.api_config_id
  project = var.project_id
  location = "us-central1"
  vpc_access_connector {
    vpc_connector_id = var.vpc_name
  }
}
