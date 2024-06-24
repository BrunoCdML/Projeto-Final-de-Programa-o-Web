from flask import render_template, redirect, url_for, session
from . import db
from .models import Cliente, Pedido, ItemPedido, Usuario
from .forms import ClienteForm, PedidoForm, LoginForm
from functools import wraps


def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('listar_clientes.html', clientes=clientes)


def adicionar_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(nome=form.nome.data, email=form.email.data, telefone=form.telefone.data)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('clientes'))
    return render_template('adicionar_cliente.html', form=form)


def excluir_cliente_view(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes'))


def listar_pedidos():
    pedidos = Pedido.query.all()
    return render_template('listar_pedidos.html', pedidos=pedidos)


def adicionar_pedido():
    form = PedidoForm()
    if form.validate_on_submit():
        pedido = Pedido(data=form.data.data, cliente_id=form.cliente_id.data)
        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for('pedidos'))
    return render_template('adicionar_pedido.html', form=form)


def excluir_pedido_view(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('pedidos'))


def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            print('Nome de usuário ou senha incorretos.', 'danger')
    return render_template('login.html', form=form)


def logout():
    session.pop('user_id', None)
    return redirect(url_for('login_route'))


def is_logged_in():
    return 'user_id' in session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login_route'))
        return f(*args, **kwargs)

    return decorated_function
