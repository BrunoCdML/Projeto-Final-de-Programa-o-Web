from flask import current_app as app, render_template
from .controllers import (login, logout, listar_clientes, adicionar_cliente, excluir_cliente_view, listar_pedidos,
                          adicionar_pedido,
                          excluir_pedido_view, login_required)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_route():
    return login()


@app.route('/logout')
def logout_route():
    return logout()


@app.route('/clientes')
@login_required
def clientes():
    return listar_clientes()


@app.route('/clientes/novo', methods=['GET', 'POST'])
@login_required
def novo_cliente():
    return adicionar_cliente()


@app.route('/clientes/excluir/<int:cliente_id>', methods=['POST'])
def excluir_cliente(cliente_id):
    return excluir_cliente_view(cliente_id)


@app.route('/pedidos')
@login_required
def pedidos():
    return listar_pedidos()


@app.route('/pedidos/novo', methods=['GET', 'POST'])
@login_required
def novo_pedido():
    return adicionar_pedido()


@app.route('/pedidos/excluir/<int:pedido_id>', methods=['POST'])
def excluir_pedido(pedido_id):
    return excluir_pedido_view(pedido_id)
