resource "google_cloud_run_service" "default" {
  name     = var.cloud_run_service
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

# Allow unauthenticated
resource "google_cloud_run_service_iam_member" "member" {
  location = google_cloud_run_service.default.location
  project  = google_cloud_run_service.default.project
  service  = google_cloud_run_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

# Load Balancing resources

resource "google_compute_global_address" "default" {
  name = "${var.name}-address"
}

resource "google_compute_global_forwarding_rule" "default" {
  name = "${var.name}-fwdrule"

  target = google_compute_target_http_proxy.default.id
  port_range = "80"
  ip_address = google_compute_global_address.default.address
}

resource "google_compute_backend_service" "default" {
  name = "${var.name}-backend"

  protocol = "HTTP"
  port_name = "http"
  timeout_sec = 30

  backend {
    group = google_compute_region_network_endpoint_group.cloudrun_neg.id
  }
}

resource "google_compute_url_map" "default" {
  name = "${var.name}-urlmap"

  default_service = google_compute_backend_service.default.id
}

resource "google_compute_target_http_proxy" "default" {
  name = "${var.name}-http-proxy"

  url_map = google_compute_url_map.default.id
}

resource "google_compute_region_network_endpoint_group" "cloudrun_neg" {
  provider = google-beta
  name = "${var.name}-neg"
  network_endpoint_type = "SERVERLESS"
  region = var.region
  cloud_run {
    service = google_cloud_run_service.default.name
  }
}
