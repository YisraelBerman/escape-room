variable "region" {
  description = "The AWS region to deploy to"
  default     = "us-east-1"
}

variable "availability_zones" {
  description = "The availability zones to use"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "subnet_cidrs" {
  description = "The CIDR blocks for the subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "dockerhub_image" {
  description = "The Docker Hub image to use"
  default     = "yisraelbdocker/bma:latest"
}

variable "ecs_cluster_name" {
  description = "The name of the ECS cluster"
  default     = "my-ecs-cluster"
}

variable "ecs_task_family" {
  description = "The family of the ECS task"
  default     = "my-web-app-task"
}

variable "ecs_service_name" {
  description = "The name of the ECS service"
  default     = "my-web-app-service"
}

variable "tags" {
  description = "A map of tags to add to all resources"
  type        = map(string)
  default     = {
    Environment = "dev"
    Project     = "MyWebApp"
  }
}
