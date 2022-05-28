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
