# IMPORTS:
from string2ascii import string2ascii
import os
import subprocess
import time
import json

#p1 = subprocess.Popen("terraform plan", shell=True)
#p1.wait()

# FUNCTIONS:
def print_colored(text, color):
    """Print text in color"""
    if color == "red":
        print("\033[91m {}\033[00m" .format(text))
    elif color == "green":
        print("\033[92m {}\033[00m" .format(text))
    elif color == "yellow":
        print("\033[93m {}\033[00m" .format(text))
    elif color == "blue":
        print("\033[94m {}\033[00m" .format(text))
    elif color == "magenta":
        print("\033[95m {}\033[00m" .format(text))
    elif color == "cyan":
        print("\033[96m {}\033[00m" .format(text))
    elif color == "white":
        print("\033[97m {}\033[00m" .format(text))
    elif color == "black":
        print("\033[98m {}\033[00m" .format(text))
    else:
        print("\033[99m {}\033[00m" .format(text))

def input_colored(text, color):
    """Input text in color"""
    if color == "red":
        return input("\033[91m {}\033[00m" .format(text))
    elif color == "green":
        return input("\033[92m {}\033[00m" .format(text))
    elif color == "yellow":
        return input("\033[93m {}\033[00m" .format(text))
    elif color == "blue":
        return input("\033[94m {}\033[00m" .format(text))
    elif color == "magenta":
        return input("\033[95m {}\033[00m" .format(text))
    elif color == "cyan":
        return input("\033[96m {}\033[00m" .format(text))
    elif color == "white":
        return input("\033[97m {}\033[00m" .format(text))
    elif color == "black":
        return input("\033[98m {}\033[00m" .format(text))
    else:
        return input("\033[99m {}\033[00m" .format(text))

def create_instance_micro(): # CHEKED
    """Create an instance of the class"""

    instance_name = input_colored("Instance name: ", "green")

    #show instaces security names
    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        print("Security groups available:")
        for i in data["security_group"]:
            print(i)
        

    security_name = input_colored("Security group: ", "green")

    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        data["instances"][instance_name] = {"instance_name": instance_name, "instance_type": "t2.micro","aws_region": "us-east-1" , "security_name": security_name}


    with open(".auto.tfvars.json", "w") as f:
        json.dump(data, f, indent=4)
    return None

def create_instance_nano(): # CHEKED
    """Create an instance of the class"""

    instance_name = input_colored("Instance name: ", "green")

    #show instaces security names
    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        print("Security groups available:")
        for i in data["security_group"]:
            print(i)

    security_name = input_colored("Security group: ", "green")

    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        data["instances"][instance_name] = {"instance_name": instance_name, "instance_type": "t2.nano","aws_region": "us-east-1" , "security_name": security_name}
        #data["instances"].append({"instance_name": instance_name, "instance_type": "t2.nano", "security_name": instance_image})


    with open(".auto.tfvars.json", "w") as f:
        json.dump(data, f, indent=4)
    return None

def delete_instance(): # CHEKED
    """Delete an instance of the class"""

    #show instaces names

    with open(".auto.tfvars.json","r") as f:
        data = json.load(f)
        print("Instances available:")
        for i in data["instances"]:
            print(i)

    instance_name = input_colored("Instance name: ", "green")

    #delete instance

    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        del data["instances"][instance_name]

    with open(".auto.tfvars.json", "w") as f:
        json.dump(data, f, indent=4)
        
        return None

def list_instances(): # CHEKED
    """List all instances"""
    with open(".auto.tfvars.json","r") as f:
        data = json.load(f)
        print("Instances available:")
        for i in data["instances"]:
            print(i)
    return None

def create_security_group(): # CHEKED
    """Create a security group"""
    security_group_name = input_colored("Security group name: ", "green")
    description = input_colored("Description: ", "green")
    from_port = input_colored("From port: ", "green")
    to_port = input_colored("To port: ", "green")
    protocol = input_colored("Protocol: ", "green")

    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        data["security_group"][security_group_name] = {
            "name": security_group_name,
            "ingress": [
                {
                    "rules": {
                        "description": description,
                        "from_port": from_port,
                        "to_port": to_port,
                        "protocol": protocol,
                        "cidr_blocks": [
                            "0.0.0.0/16"
                        ],
                        "ipv6_cidr_blocks": None,
                        "prefix_list_ids": None,
                        "self": None,
                        "security_groups": None
                    }
                }
            ],
            "egress": [
                {
                    "rules": {
                        "description": "descr_egress",
                        "from_port": "0",
                        "to_port": "0",
                        "protocol": "-1",
                        "cidr_blocks": [
                            "0.0.0.0/0"
                        ],
                        "ipv6_cidr_blocks": [
                            "::/0"
                        ],
                        "prefix_list_ids": None,
                        "self": None,
                        "security_groups": None
                    }
                }
            ]
        }
    with open(".auto.tfvars.json", "w") as f:
        json.dump(data, f, indent=4)
    return None

def delete_security_group(): # CHEKED
    """Delete a security group"""
    #show security groups names
    with open(".auto.tfvars.json","r") as f:
        data = json.load(f)
        print("Security groups available:")
        for i in data["security_group"]:
            print(i)

    security_group_name = input_colored("Security group name: ", "green")

    #delete security group
    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        del data["security_group"][security_group_name]

    with open(".auto.tfvars.json", "w") as f:
        json.dump(data, f, indent=4)
        
        return None

def list_security_groups(): # CHEKED
    #show security groups names
    with open(".auto.tfvars.json","r") as f:
        data = json.load(f)
        print("Security groups available:")
        for i in data["security_group"]:
            print(i)

    return None

def create_users(): # CHEKED
    """Create a user"""
    user_name = input_colored("User name: ", "green")
    restriction_name = input_colored("Restriction name: ", "green")

    specific_restrictions = input_colored("Apply restrictions to user? (y/n): ", "green")

    list_actions = []
    list_resources = []
    if specific_restrictions == "y":
        action = input_colored("Actions (use comma [,] between actions): ", "green")
        list_actions = action.split(",")
        resources = input_colored("Resources (use comma [,] between resources): ", "green")
        list_resources = resources.split(",")
    else:
        list_actions = ["*"]
        list_resources = ["*"]

    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        data["users"].append({
            "username": user_name,
            "restrictions": {
                "restriction_name": restriction_name,
                "actions": list_actions,
                "resources": list_resources
            }
        })


    with open(".auto.tfvars.json", "w") as f:
        json.dump(data, f, indent=4)
    return None

def delete_users(): # CHEKED
    """Delete a user"""
    
    #show users names
    with open(".auto.tfvars.json","r") as f:
        data = json.load(f)
        print("Users available:")
        for i in data["users"]:
            print(i["username"])

    user_name = input_colored("User name: ", "green")

    #delete user
    with open(".auto.tfvars.json","r+") as f:
        data = json.load(f)
        for i in data["users"]:
            if i["username"] == user_name:
                data["users"].remove(i)

    with open(".auto.tfvars.json", "w") as f:
        json.dump(data, f, indent=4)
    
    return None

def list_users(): # CHEKED
    '''Show users names'''
    with open(".auto.tfvars.json","r") as f:
        data = json.load(f)
        print("Users available:")
        for i in data["users"]:
            print(i["username"])
    
    return None

# STATES MACHINE:
state = 1
while True:
    
        # STATE 1: START
        if state == 1:
            terraform_init = subprocess.Popen("terraform init", shell=True)
            terraform_init.wait()
            os.system("cls")
            
            print_colored(string2ascii("\nPROJETO DE CLOUD\n"), "blue")
            print_colored('-'*60, "white")
            state = 2
    
        # STATE 2: WAITING FOR INPUT
        elif state == 2:
            
            print("")
            # Get input
            print_colored("Enter '1' to create instance", "cyan")
            print_colored("Enter '2' to delete instance", "cyan")
            print_colored("Enter '3' to list all instances", "cyan")
            print_colored("Enter '4' to create security group", "magenta")
            print_colored("Enter '5' to delete security group", "magenta")
            print_colored("Enter '6' to list all security group", "magenta")
            print_colored("Enter '7' to create users", "yellow")
            print_colored("Enter '8' to delete users", "yellow")
            print_colored("Enter '9' to list all users", "yellow")
            print_colored("Enter '10' to apply changes", "green")
            print_colored("Enter '11' to exit",'red')
            selection = input("Input: ")
            print("\n")
            

            # input confirmation
            if selection in ['1', '2', '3', '4','5','6','7','8','9','10','11']:
                garantia = input_colored("Are you sure? (y/n): ", "yellow")
                if garantia == "y":
                    pass
                else:
                    state = 2
                    continue
            
            # switch states depending on input
            if selection == '1':
                state = 3

            elif selection == '2':
                state = 4

            elif selection == '3':
                state = 5

            elif selection == '4':
                state = 6

            elif selection == '5':
                state = 7
            
            elif selection == '6':
                state = 8
            
            elif selection == '7':
                state = 9

            elif selection == '8':
                state = 10
            
            elif selection == '9':
                state = 11

            elif selection == '10':
                state = 12

            elif selection == '11':
                state = 13
            

            else:
                skip = input_colored("Invalid input. Press enter to continue", 'red')
                state = 2
            

        # STATE 3: create
        elif state == 3:
            print_colored("Choose host configuration:", "cyan")
            print_colored("Enter '1' for t2.micro", "cyan")
            print_colored("Enter '2' for t2.nano", "cyan")
            option_creation = input_colored("Input: ", 'cyan')
            if option_creation == '1':
                create_instance_micro()
            elif option_creation == '2':
                create_instance_nano()
            
            state = 2
    
        # STATE 4: delete
        elif state == 4:
            delete_instance()
            state = 2
    
        # STATE 5: list all instances
        elif state == 5:
            list_instances()
            time.sleep(1)
            state = 2

        # STATE 6: create security group
        elif state == 6:
            create_security_group()
            state = 2

        # STATE 7: delete security group
        elif state == 7:
            delete_security_group()
            state = 2

        # STATE 8: list all security groups
        elif state == 8:
            list_security_groups()
            time.sleep(1)
            state = 2

        # STATE 9: create users
        elif state == 9:
            create_users()
            state = 2

        # STATE 10: delete users
        elif state == 10:
            delete_users()
            state = 2

        # STATE 11: list all users
        elif state == 11:
            list_users()
            time.sleep(1)
            state = 2
        
        # STATE 12: apply
        elif state == 12:
            terraform_apply = subprocess.Popen('terraform apply -var-file="secret.tfvars"', shell=True)
            terraform_apply.wait()
            state = 2

        # STATE 13: exit
        elif state == 13:
            print("Exiting...")
            time.sleep(1)
            break
