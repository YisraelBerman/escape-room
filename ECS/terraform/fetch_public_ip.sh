#!/bin/bash

# Use environment variables for the cluster and service names
CLUSTER_NAME=${CLUSTER_NAME}
SERVICE_NAME=${SERVICE_NAME}

# Wait for the task to start and the network interface to be assigned
sleep 60

TASK_ARN=$(aws ecs list-tasks --cluster $CLUSTER_NAME --service-name $SERVICE_NAME --query 'taskArns[0]' --output text)
ENI_ID=$(aws ecs describe-tasks --cluster $CLUSTER_NAME --tasks $TASK_ARN --query 'tasks[0].attachments[0].details[?name==`networkInterfaceId`].value' --output text)
PUBLIC_IP=$(aws ec2 describe-network-interfaces --network-interface-ids $ENI_ID --query 'NetworkInterfaces[0].Association.PublicIp' --output text)

echo " "
echo " "
echo " "

echo "Public IP: $PUBLIC_IP"

echo " "
echo " "
echo " "
