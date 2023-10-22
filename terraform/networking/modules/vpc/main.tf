resource "google_compute_network" "getwib" {
  name                    = var.vpc_name
  auto_create_subnetworks = false
  project                 = var.project_id
}

resource "google_compute_subnetwork" "subnets" {
  for_each                 = var.subnets
  name                     = each.key
  region                   = each.value["region"]
  ip_cidr_range            = each.value["ip_cidr_range"]
  private_ip_google_access = true
  network                  = google_compute_network.getwib.self_link
  project                  = var.project_id
}

resource "google_compute_firewall" "allow_all" {
  name    = "${var.vpc_name}-allow-all"
  network = google_compute_network.getwib.self_link
  allow {
    protocol = "tcp"
    ports    = ["0-65535"]
  }
  allow {
    protocol = "udp"
    ports    = ["0-65535"]
  }
  allow {
    protocol = "icmp"
  }
  source_tags = ["getwib-backend"]
}

resource "google_compute_global_address" "private_ip_address" {
  name          = "${var.vpc_name}-private-ip-address"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = google_compute_network.getwib.self_link
  project       = var.project_id
}

resource "google_service_networking_connection" "private_vpc_connection" {
  network                 = google_compute_network.getwib.self_link
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
  depends_on              = [google_project_service.service_networking]
}

resource "google_project_service" "service_networking" {
  service            = "servicenetworking.googleapis.com"
  disable_on_destroy = false
}
