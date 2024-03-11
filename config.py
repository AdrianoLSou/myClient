import os

class Config:
    # Configurações gerais do aplicativo
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'mysql://seu_usuario_mysql:sua_senha_mysql@localhost/seu_banco_de_dados'
    SQLALCHEMY_TRACK_MODIFICATIONS = False