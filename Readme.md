
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
abra o terminal e digite:
git clone https://github.com/BrunoCdML/Projeto-Final-de-Programa-o-Web.git

2. Entre no repositório:
cd Projeto-Final-de-Programa-o-Web.git

3. Caso use o VSCode, digite code . no terminal que irá abrir já no IDE.

4. Siga os passos abaixo, digite todos eles no terminal

    1.python -m venv venv
    2.source venv/bin/activate  # No Windows use: venv\\Scripts\\activate
    3.pip install -r requirements.txt
   
5. Aqui vai um vídeo de como configurar o banco de dados para usar na sua máquina:
   https://www.youtube.com/watch?v=HWYLFESRfVk&ab_channel=BrunoCardoso

CREATE DATABASE IF NOT EXISTS distribuidora_legal;
USE distribuidora_legal;

CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(150) NOT NULL
);



