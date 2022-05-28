provider "google" {
    # Make service account and CREATE JSON key
  credentials = file("./.json") #directory file diisi ama letak JSON key
  project     = "PROJECT-ID"
  region      = "us-central1"
  version     = "~> 2.5.0"
}

