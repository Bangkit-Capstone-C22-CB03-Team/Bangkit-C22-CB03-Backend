module "lb-http" {
  source  = "GoogleCloudPlatform/lb-http/google//modules/serverless_negs"
  version = "~> 6.2.0"
  name    = var.lb-name
  project = var.project_id

#   ssl                             = var.ssl
#   managed_ssl_certificate_domains = [var.domain]
#   https_redirect                  = var.ssl

  backends = {
    default = {
      description = null
      groups = [
        {
          group = google_compute_region_network_endpoint_group.serverless_neg.id
        }
      ]
      enable_cdn              = false
      security_policy         = null
      custom_request_headers  = null
      custom_response_headers = null

      iap_config = {
        enable               = false
        oauth2_client_id     = ""
        oauth2_client_secret = ""
      }
      log_config = {
        enable      = false
        sample_rate = null
      }
    }
  }
}

resource "google_compute_region_network_endpoint_group" "serverless_neg" {
  provider              = google-beta
  name                  = "serverless-neg"
  network_endpoint_type = "SERVERLESS"
  region                = var.region
  cloud_run {
    service = google_cloud_run_service.default.name
  }
}

resource "google_cloud_run_service" "default" {
  name     = "chatbot"
  location = var.region
  project  = var.project_id
  metadata {
    annotations = merge(
        {
            "run.googleapis.com/ingress" = var.ingress
        }
    )
  }
  template {
    spec {
      containers {
        image = "us-central1-docker.pkg.dev/qwiklabs-gcp-03-65e72cae822e/chatbot-regis/chatbot:0.1"
        ports {
          container_port = 8080
        }
        resources {
          limits = {
            cpu    = 4
            memory = "8Gi"
          }
        }
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}


# Allow unauthenticated
resource "google_cloud_run_service_iam_member" "member" {
  location = google_cloud_run_service.default.location
  project  = google_cloud_run_service.default.project
  service  = google_cloud_run_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}