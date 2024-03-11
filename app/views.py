from flask import request
from flask_restful import Resource
from .models import Vendedor, Cliente, db

class VendedorResource(Resource):
    def post(self):
        # Lógica para cadastrar um vendedor via API
        pass

# Recursos para clientes também
    
# Rota para a API RESTful
# from flask_restful import Resource
# from .models import Vendedor, Cliente

class ComissaoResource(Resource):
    def post(self, vendedor_id):
        try: # Obter o vendedor pelo id
            vendedor = vendedor.query.get(vendedor_id)
            if not vendedor:
                return {'error': 'Vendedor não encontrado'}, 404
            # Obter o valor da venda (implementar a lógica para isso)
            valor_venda = float(request.form['valor_venda'])
            # Calcular a comissão (7% do valor da venda)
            comissao = valor_venda * 0.07
            # Atualizar o valor da comissão no banco de dados
            vendedor.comissao_vendedor = comissao
            db.session.commit()

            return {'message': f'Comissão calculada: R${comissao: .2f}'}, 200
        
        except Exception as e:
            return {'error': str(e)}, 500 

            