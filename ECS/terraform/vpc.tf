resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  tags       = var.tags
}

resource "aws_subnet" "subnet1" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.subnet_cidrs[0]
  availability_zone = var.availability_zones[0]
  map_public_ip_on_launch = true
  tags              = var.tags
}

resource "aws_subnet" "subnet2" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.subnet_cidrs[1]
  availability_zone = var.availability_zones[1]
  map_public_ip_on_launch = true
  tags              = var.tags
}

resource "aws_security_group" "ecs" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = var.tags
}

# Internet Gateway
resource "aws_internet_gateway" "ecs_igw" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "ECS IGW"
  }
}


# Route Tables and Associations for Public and Private Subnets
resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.ecs_igw.id
  }
  tags = {
    Name = "Public Route Table"
  }
}

resource "aws_route_table_association" "public_rta_a" {
  subnet_id      = aws_subnet.subnet1.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_route_table_association" "public_rta_b" {
  subnet_id      = aws_subnet.subnet2.id
  route_table_id = aws_route_table.public_route_table.id
}