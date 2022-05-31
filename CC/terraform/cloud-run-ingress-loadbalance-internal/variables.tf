variable "project_id" {
  type = string
}

variable "region" {
  description = "Location for load balancer and Cloud Run resources"
  default     = "us-central1"
  type = string
}

variable "zone" {
  type = string
  default = "us-central1-a"
}

variable "ingress" {
  type = string
  default = "all"
  description = "Ingress setting for the service. Allowed values: 'all','internal','internal-and-cloud-load-balancing'"
}

variable "ssl" {
  description = "Run load balancer on HTTPS and provision managed certificate with provided `domain`."
  type        = bool
  default     = false
}

variable "domain" {
  description = "Domain name to run the load balancer on. Used if `ssl` is `true`."
  type        = string
}

variable "lb-name" {
  description = "Name for load balancer and associated resources"
  default     = "run-lb"
}