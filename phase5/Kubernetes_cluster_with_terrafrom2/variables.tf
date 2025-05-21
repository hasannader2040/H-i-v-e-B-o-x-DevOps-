variable "aws_region" {
  default = "us-east-1"  # Choose a free-tier eligible region
}

variable "cluster_name" {
  default = "my-k8s-cluster"
}

variable "node_group_size" {
  default = 2  # Free tier supports small clusters
}
