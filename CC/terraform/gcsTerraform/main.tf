resource "random_id" "instance_id" {
  byte_length = 4
}

resource "google_storage_bucket" "default" {
  name = "bucket-model-${random_id.instance_id.hex}"
  force_destroy = false
  location      = "US"
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
  lifecycle_rule {
    condition {
      days_since_noncurrent_time  = 20
    }
    action {
      type = "Delete"
    }
  }
}
