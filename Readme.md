
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

-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS distribuidora_legal;
USE distribuidora_legal;

-- Criação da tabela Usuario
CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(150) NOT NULL
);

-- Criação da tabela Cliente
CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

-- Criação da tabela Produto
CREATE TABLE Produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT NOT NULL
);

-- Criação da tabela Pedido
CREATE TABLE Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATETIME NOT NULL,
    cliente_id INT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
);

-- Criação da tabela ItemPedido
CREATE TABLE ItemPedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quantidade INT NOT NULL,
    preco_total DECIMAL(10, 2) NOT NULL,
    produto_id INT NOT NULL,
    pedido_id INT NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES Produto(id),
    FOREIGN KEY (pedido_id) REFERENCES Pedido(id)
);

-- Criação da tabela Fornecedor
CREATE TABLE Fornecedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

-- Populando a tabela Cliente
INSERT INTO Cliente (nome, email, telefone) VALUES
('João Silva', 'joao.silva@example.com', '123456789'),
('Maria Oliveira', 'maria.oliveira@example.com', '987654321'),
('Carlos Souza', 'carlos.souza@example.com', '555666777'),
('Ana Santos', 'ana.santos@example.com', '444555666'),
('Pedro Lima', 'pedro.lima@example.com', '333444555');

-- Populando a tabela Produto
INSERT INTO Produto (nome, preco, estoque) VALUES
('Produto A', 10.50, 100),
('Produto B', 20.75, 200),
('Produto C', 30.00, 150),
('Produto D', 40.25, 80),
('Produto E', 50.50, 60);

-- Populando a tabela Pedido
INSERT INTO Pedido (data, cliente_id) VALUES
('2024-06-19 10:00:00', 1),
('2024-06-19 11:00:00', 2),
('2024-06-19 12:00:00', 3),
('2024-06-19 13:00:00', 4),
('2024-06-19 14:00:00', 5);

-- Populando a tabela ItemPedido
INSERT INTO ItemPedido (quantidade, preco_total, produto_id, pedido_id) VALUES
(2, 21.00, 1, 1),
(1, 20.75, 2, 2),
(3, 90.00, 3, 3),
(4, 161.00, 4, 4),
(1, 50.50, 5, 5);

-- Populando a tabela Fornecedor
INSERT INTO Fornecedor (nome, telefone) VALUES
('Fornecedor X', '111222333'),
('Fornecedor Y', '444555666'),
('Fornecedor Z', '777888999'),
('Fornecedor W', '000111222'),
('Fornecedor V', '333444555');

-- Populando a tabela Usuario
INSERT INTO Usuario (username, password) VALUES
('admin', 'admin'), -- senha: admin123
('user1', 'abc123'), -- senha: user123
('user2', 'dfg456'); -- senha: user456




