# regras de negocio relacionadas a usuarios
# CRUD - Create, Read, Update, Delete
from ..models.usuario_model import UsuarioModel
from ..entities.usuario_entity import Usuario
from src import db


def cadastrar_usuario(usuario):
    usuario_db = Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.gen_senha(usuario.senha)
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

def listar_usuarios():
    usuarios_encontrado = UsuarioModel.query.all()
    
    # retorna a lista de usuarios encontrados
    return usuarios_encontrado

def listar_usuario_id(id):
    usuario_encontrado = UsuarioModel.query.get(id)

    # retorna o usuario encontrado
    return usuario_encontrado

def listar_usuario_email(email):
    usuario_encontrado = UsuarioModel.query.filter_by(email=email).first()
    
    # retorna o usuario encontrado
    return usuario_encontrado

def editar_usuario(id, usuario):
    usuario_encontrado = UsuarioModel.query.get(id)

    
    usuario_encontrado.nome = usuario.nome

    if usuario.senha:
        usuario_encontrado.gen_senha(usuario.senha)

    db.session.commit()

    return usuario_encontrado


def deletar_usuario(id):
    usuario_encontrado = UsuarioModel.query.get(id)
    db.session.delete(usuario_encontrado)
    db.session.commit()

    return usuario_encontrado