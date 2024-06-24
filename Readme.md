
# Distribuidora Legal

Distribuidora Legal é uma aplicação web desenvolvida com Flask para gerenciar uma distribuidora. A aplicação permite gerenciar clientes, pedidos e inclui funcionalidades de autenticação (login/logout). A aplicação utiliza Bootstrap para a interface de usuário e SQLAlchemy para a interação com o banco de dados MySQL.

## Funcionalidades

- Gerenciamento de clientes (CRUD)
- Gerenciamento de pedidos (CRUD)
- Autenticação de usuários (login/logout)
- Proteção de rotas para permitir acesso apenas a usuários autenticados

## Tecnologias Utilizadas

- Python 3
- Flask
- SQLAlchemy
- Flask-WTF
- Bootstrap
- MySQL


## Instalação

### Pré-requisitos

- Python 3.x
- MySQL

### Passos

1. Clone o repositório:

```sh
https://github.com/BrunoCdML/Projeto-Final-de-Programa-o-Web.git
cd Projeto-Final-de-Programa-o-Web.git

python -m venv venv
source venv/bin/activate  # No Windows use: venv\\Scripts\\activate

pip install -r requirements.txt

CREATE DATABASE IF NOT EXISTS distribuidora_legal;
USE distribuidora_legal;

CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(150) NOT NULL
);



