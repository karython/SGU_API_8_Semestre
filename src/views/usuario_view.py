# POST - PUT - DELETE - GET
# rotas que precisam de ID - editar, excluir, listar por id
# rotas que não precisam de ID - listar todos os usuarios, cadastrar usuario
# classes - herdar de Resource

from flask_restful import Resource
from marshmallow import ValidationError
from src.schemas.usuario_schema import UsuarioSchema
from src.entities import usuario_entity
from flask import request, jsonify, make_response
from src.services import usuario_service
from src import api

# lidar com todos os usuarios
class UsuarioList(Resource):
    # listar todos os usuarios
    def get(self):
        usuarios = usuario_service.listar_usuarios()
        schema = UsuarioSchema(many=True)

        if not usuarios:
            return make_response(jsonify({'message': 'Nenhum usuario encontrado'}), 404)

        return make_response(jsonify(schema.dump(usuarios)), 200)
    

    # cadastrar usuario
    def post(self):
        schema = UsuarioSchema()

        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        if usuario_service.listar_usuario_email(dados['email']):
            return make_response(jsonify({'message': 'Email já cadastrado!'}), 400)

        try:
            novo_usuario = usuario_entity.Usuario(
                nome=dados['nome'],
                email=dados['email'],
                senha=dados['senha']
            )

            resultado = usuario_service.cadastrar_usuario(novo_usuario)

            return make_response(jsonify(schema.dump(resultado)), 201)
        except Exception as e:
            return make_response(jsonify({'message': 'Erro ao cadastrar usuario', 'error': str(e)}), 500)

# criação da rota de usuarios
# cadastra e lista todos
api.add_resource(UsuarioList, '/usuarios')


# lidar com um usuario especifico
class UsuarioResource(Resource):
    # listar usuario por id
    def get(self, id):
        usuario_encontrado = usuario_service.listar_usuario_id(id)
        schema = UsuarioSchema()

        if not usuario_encontrado:
            return make_response(jsonify({'messsage' : 'Usuario não encontrado!'}), 404)
        
        try:
            return make_response(jsonify(schema.dump(usuario_encontrado)), 200)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
            
    # editar usuario
    def put(self, id):
        usuario_encontrado = usuario_service.listar_usuario_id(id)
        schema = UsuarioSchema()

        if not usuario_encontrado:
            return make_response(jsonify({'messsage' : 'Usuario não encontrado!'}), 404)
        
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        try:
            resultado = usuario_service.editar_usuario(id, dados)
            return make_response(jsonify(schema.dump(resultado)), 200)
        except Exception as e:
            return make_response(jsonify({'message': 'Erro ao editar usuario', 'error': str(e)}), 400)
    
    # excluir usuario
    def delete(self, id):
        usuario_encontrado = usuario_service.listar_usuario_id(id)

        if not usuario_encontrado:
            return make_response(jsonify({'messsage' : 'Usuario não encontrado!'}), 404)
        
        try:
            usuario_service.deletar_usuario(id)
            return make_response(jsonify({'message':'Usuario excluido com sucesso!'}), 200)
        except Exception as e:
            return make_response(jsonify({'message': 'Erro ao excluir usuario', 'error': str(e)}), 500)

# criação da rota de usuario
# edita, deleta e lista por id
api.add_resource(UsuarioResource, '/usuarios/<int:id>')