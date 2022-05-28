output "cloud_run_url" {
  value = google_cloud_run_service.chatbot_cloud_run.traffic.*.url
}

output "status" {
  value = google_cloud_run_service.chatbot_cloud_run.status
}
