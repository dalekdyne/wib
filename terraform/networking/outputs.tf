output "vpc" {
  value = module.vpc.vpc_self_link
}

output "subnets" {
  value = module.vpc.subnets_self_links
}
