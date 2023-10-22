output "vpc_self_link" {
  description = "The URI of the created VPC."
  value       = google_compute_network.getwib.self_link
}

output "subnets_self_links" {
  description = "The URIs of the created subnets."
  value       = { for name, subnet in google_compute_subnetwork.subnets : name => subnet.self_link }
}
