resource "null_resource" "fetch_public_ip" {
  provisioner "local-exec" {
    command = "./fetch_public_ip.sh"
    environment = {
      CLUSTER_NAME = aws_ecs_cluster.main.name
      SERVICE_NAME = aws_ecs_service.web_app_service.name
    }
  }

  # Make sure this runs after the ECS service is created
  depends_on = [
    aws_ecs_service.web_app_service
  ]
}
