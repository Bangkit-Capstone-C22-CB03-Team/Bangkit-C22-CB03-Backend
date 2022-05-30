output "cloud_run_url" {
  value = google_cloud_run_service.chatbot_cloud_run.status.0.url
}

output "load-balancer-ip" {
  value = module.lb-http.external_ip
}
