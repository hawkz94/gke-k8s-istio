provider "google" {
  credentials = file("./credentials.json")
  project     = ""
  region      = var.location
  version     = "~> 2.5.0"
}