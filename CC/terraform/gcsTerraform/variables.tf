variable "project_id" {
  type = string
}

variable "zone" {
  type    = string
  default = "us-central1-a"
}

variable "region" {
  description = "Location for load balancer and Cloud Run resources"
  default     = "us-central1"
  type        = string
}