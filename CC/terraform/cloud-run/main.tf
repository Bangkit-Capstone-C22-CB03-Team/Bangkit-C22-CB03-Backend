# Load Balancer for Cloud Run

module "lb-http" {
  source  = "GoogleCloudPlatform/lb-http/google//modules/serverless_negs"
  version = "~> 6.2.0"
  name    = var.lb_name
  project = var.project_id

  # for https
  ssl                             = var.ssl
  managed_ssl_certificate_domains = [var.domain]
  https_redirect                  = var.ssl

  backends = {
    default = {
      description = null
      groups = [
        {
          group = google_compute_region_network_endpoint_group.chatbot_neg.id
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

resource "google_compute_region_network_endpoint_group" "chatbot_neg" {
  provider              = google-beta
  name                  = "chatbot-network-endpoint-group"
  network_endpoint_type = "SERVERLESS"
  region                = var.region
  cloud_run {
    service = google_cloud_run_service.chatbot_cloud_run.name
  }
}

# Cloud Run Configuration

resource "google_cloud_run_service" "chatbot_cloud_run" {
  name     = var.cloud_run_service_name
  location = var.region

  template {
    spec {
      containers {
        image = var.image
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

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location = google_cloud_run_service.chatbot_cloud_run.location
  project  = google_cloud_run_service.chatbot_cloud_run.project
  service  = google_cloud_run_service.chatbot_cloud_run.name

  policy_data = data.google_iam_policy.noauth.policy_data
}
