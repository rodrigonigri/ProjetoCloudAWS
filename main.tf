terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0" 
}

provider "aws" {
    region = var.aws_region
    access_key = var.access_key
    secret_key = var.secret_key
}


resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "Main"
  }
}

resource "aws_security_group" "security_group" {
  vpc_id   = aws_vpc.main.id
  for_each = var.security_group
  name     = each.value.name
  ingress  = [for rule in each.value.ingress : rule.rules]
  egress   = [for rule in each.value.egress : rule.rules]
}

resource "aws_instance" "app_server" {
  for_each      = var.instances
  ami           = var.instance_ami
  instance_type = each.value.instance_type
  subnet_id = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.security_group[each.value.security_name].id]
  tags = {
    Name = "${each.value.instance_name}"
  }

}



resource "aws_iam_user" "user_test" {
    for_each = { for user in var.users : user.username => user }
    name     = each.value.username
}

resource "aws_iam_access_key" "iam_access_key" {
    for_each = { for user in var.users : user.username => user }
    user = aws_iam_user.user_test[each.value.username].name
}

data "aws_iam_policy_document" "ec2_policy" {
    for_each = {for user in var.users : user.username => user}
    policy_id = each.value.username
    statement {
        effect = "Allow"
        sid = "VisualEditor0"
        actions = each.value.restrictions.actions
        resources = each.value.restrictions.resources
    }
}

resource "aws_iam_policy" "ec2_policy" {
    for_each = { for user in var.users : user.username => user }
    name        = each.value.restrictions.restriction_name
    policy      = data.aws_iam_policy_document.ec2_policy[each.value.username].json
}

resource "aws_iam_user_policy_attachment" "user_policy_attachment" {
    for_each = { for user in var.users : user.username => user }
    user       = aws_iam_user.user_test[each.value.username].name
    policy_arn = aws_iam_policy.ec2_policy[each.value.username].arn
}

resource "aws_iam_user_login_profile" "profile" {
    for_each                = { for user in var.users : user.username => user }
    user                    = aws_iam_user.user_test[each.value.username].name
    password_length         = 18
    password_reset_required = true
}