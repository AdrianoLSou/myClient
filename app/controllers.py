from flask import Blueprint, request
from .models import Vendedor, Cliente

vendedor_bp = Blueprint('vendedor', _name_)

@vendedor_bp.route('/vendedores', methods=['POST'])
def cadastrar_vendedor():
    # Lógica para cadastrar um vendedor
    pass

# Rotas e controladores para clientes também

# Rotas para cálculo de comissão
from flask import Blueprint, request, jsonify
from .models import Vendedor, Cliente, db

comissao_bp = Blueprint('comissao', _name_)

@comissao_bp.route('/calcular_comissao/<int:vendedor_id>', methods=['POST'])
def calcular_comissao(vendedor_id):
    try:
        # Obtenha o vendedor pelo ID
        vendedor = Vendedor.query.get(vendedor_id)
        if not vendedor:
            return jsonify({'error': 'Vendedor não encontrado'}), 404

        # Obtenha o valor da venda do cliente (você precisa implementar a lógica para isso)
        valor_venda = float(request.form['valor_venda'])

        # Calcule a comissão (7% do valor da venda)
        comissao = valor_venda * 0.07

        # Atualize o valor da comissão no banco de dados
        vendedor.comissao_vendedor = comissao
        db.session.commit()

        return jsonify({'message': f'Comissão calculada: R${comissao:.2f}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500