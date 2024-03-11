from flask_restful import Resource
from .models import Vendedor, Cliente

class VendedorResource(Resource):
    def post(self):
        # Lógica para cadastrar um vendedor via API
        pass

# Recursos para clientes também
    
# Rota para a API RESTful
from flask_restful import Resource
from .models import Vendedor, Cliente

class ComissaoResource(Resource):
    def post(self, vendedor_id):
        # Lógica para calcular a comissão (mesmo código do exemplo acima)
        # Retorne uma resposta JSON com a comissão calculada
        return {'message': 'Comissão calculada com sucesso!'}, 200    