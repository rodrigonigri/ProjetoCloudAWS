# Projeto Semestral Computação em Nuvem
### Feito por Rodrigo Nigri Griner


## Proposta:
A proposta desse projeto é criar uma interface amigavel para o usuário, que primeiramente permita a criação de uma VPC e subnet, e dentro delas, possibilite a criação de diversas instâncias associadas a security groups. Além disso, o usuário poderá criar users no IAM, e associar esses users a grupos de permissões, para que possam acessar as instâncias criadas.

## Tecnologias utilizadas:

- **Python**
- **Terraform**
- **AWS**

## Como funciona o terraform:

O Terraform é uma ferramenta open source que permite criar e alterar partes da infraestrutura em nuvem através de blocos de código, o que abrange o conceito de infraestrutura como código (IaC : "Infrastructure as code"). 

Quando é executado o comando `terraform apply`, o terraform irá ler o arquivo main.tf, que por sua vez lê o arquivo variables.tf, e o arquivo .auto.tfvars.json, e em seguida ele compara o estado atual da infraestrutura com o estado desejado, e então ele cria, altera ou destrói os recursos necessários para que o estado atual seja igual ao estado desejado.

## Como funciona o projeto:

De maneira geral, o projeto foi feito no arquivo main.py. Nele utilizando a biblioteca subprocess, é possível rodar os comandos do terraform, e assim criar as instâncias, VPCs, subnets, security groups, etc. 

O terraform é dividido em 3 principais arquivos, sendo eles:

- `main.tf`: Arquivo principal, onde são criadas as instâncias, VPCs, subnets, security groups, etc.
- `variables.tf`: Arquivo onde são definidas as variáveis que serão utilizadas no arquivo main.tf.
- `.auto.tfvars.json`: Arquivo onde são definidas as variáveis que serão utilizadas no arquivo variables.tf.

## Como rodar o projeto:

- Primeiramente, é necessário ter o terraform instalado na máquina, e configurar as credenciais da AWS. Para isso, basta seguir o tutorial do próprio terraform: https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started.

- Será necessário baixar todas as dependências do projeto presentes no arquivo `requirements.txt`.

- **ETAPA MUITO IMPORTANTE!!!** Será necessário prencher o arquivo `secret.tfvars` **(NUNCA PUBLIQUE OU COMPARTILHE ESSAS CHAVES!!!):** 

``` terraform
access_key = "sua acces_key"
secret_key = "sua secret_key"
```

- Para executar os arquivos terraform genéricos, é necessário rodar os seguintes comandos no terminal:

```
$ terrafomr init
$ terraform plan
$ terraform apply
```

- Porém esses comandos já fazem parte do arquivo main.py, então basta rodar o comando abaixo e seguir as instruções do terminal:

```
$ python main.py
```

- **Se divirta! :D**
