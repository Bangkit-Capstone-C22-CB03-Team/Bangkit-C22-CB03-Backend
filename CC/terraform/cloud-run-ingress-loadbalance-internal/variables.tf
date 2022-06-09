variable "project_id" {
  type = string
}

variable "name" {
  description = "The name prefix for load balancer resources"  
  type = string
  default = "chatbot"
}

variable "region" {
  description = "Location for load balancer and Cloud Run resources"
  default     = "us-central1"
  type        = string
}

variable "zone" {
  type    = string
  default = "us-central1-a"
}

variable "cloud_run_service" {
  description = "the name of cloud run service"
  type = string
  default = "chatbot-tvlk"
}

variable "ingress" {
  type        = string
  default     = "all"
  description = "Ingress setting for the service. Allowed values: 'all','internal','internal-and-cloud-load-balancing'"
}

# variable "ssl" {
#   description = "Run load balancer on HTTPS and provision managed certificate with provided `domain`."
#   type        = bool
#   default     = false
# }

# variable "domain" {
#   description = "Domain name to run the load balancer on. Used if `ssl` is `true`."
#   type        = string
#   default = null
# }

# variable "lb-name" {
#   description = "Name for load balancer and associated resources"
#   default     = "run-lb"
# }

# variable "cloud_run_service_name" {
#   type = string
# }

variable "image" {
  type = string
  description = "Name of the dockerize image pushed in artifact registry"
}
