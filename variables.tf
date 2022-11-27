variable "aws_region" {
    type        = string
    description = "AWS region"
    default     = "us-east-1"
}

variable "access_key" {
  description = "AWS access key"
  type        = string
  sensitive = true
}

variable "secret_key" {
  description = "AWS secret key"
  type        = string
  sensitive = true
}



variable "instance_ami" {
    type = string
    description = "AMI ID"
    default = "ami-0b0dcb5067f052a63"
}

variable "instance_type" {
    type        = string
    description = "AWS instance type"
    default     = "t3.micro"
}

variable "instance_tags" {
    type = map(string)
    description = "AWS instance tags"
    default = {
        Name = "Ubunto"
        Projeto = "Terraform"
    }
}

variable "security_group" {
  type = map(object({

    name = string

    ingress = list(map(object({
      description      = string
      from_port        = number
      to_port          = number
      protocol         = string
      cidr_blocks      = list(string)
      ipv6_cidr_blocks = list(string)
      prefix_list_ids  = list(string)
      self             = bool
      security_groups  = list(string)
    })))

    egress = list(map(object({
      description      = string
      from_port        = number
      to_port          = number
      protocol         = string
      cidr_blocks      = list(string)
      ipv6_cidr_blocks = list(string)
      prefix_list_ids  = list(string)
      self             = bool
      security_groups  = list(string)
  })))

}))

}

variable "instances" {
  description = "Instances"
  type        = map(object({
    instance_name = string
    instance_type = string
    aws_region = string
    security_name = string
  }))
}


variable "users" {
  type = list(object({
    username = string
    restrictions = object ({
      restriction_name = string
      actions = list(string)
      resources = list(string)
    })
  }))
  default = [
    {
      username = "user1"
      restrictions = {
        restriction_name = "restriction1"
        actions = ["*"]
        resources = ["*"]
      }
    }
  ]
}