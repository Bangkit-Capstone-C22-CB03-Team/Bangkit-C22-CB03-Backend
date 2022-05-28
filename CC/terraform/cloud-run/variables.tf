variable "project_id" {
  type = string

}

variable "region" {
  type    = string
  default = "us-central1"
}

variable "zone" {
  type    = string
  default = "us-central1-a"
}

variable "cloud_run_service_name" {
  type = string
}

variable "image" {
  type = string
}
