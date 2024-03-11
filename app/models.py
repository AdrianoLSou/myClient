from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vendedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)  # Sobrenome do vendedor
    data_nascimento = db.Column(db.Date, nullable=False)  # Data de nascimento
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)  # Senha (criptografada)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)  # Sobrenome do cliente
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    foto_cliente = db.Column(db.String(200))  # Caminho para a foto do cliente
    produto_vendido = db.Column(db.String(100), nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    valor_venda = db.Column(db.Float, nullable=False)  # Valor da venda
    comissao_vendedor = db.Column(db.Float)  # Valor da comissão do vendedor (calculado)
    relato_cliente = db.Column(db.Text)  # Histórico do cliente