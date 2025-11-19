# criar a tabela
from src import db
from passlib.hash import pbkdf2_sha256 as sha256

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)

    def gen_senha(self, senha):
        self.senha = sha256.hash(senha)

    # verificar a senha
    def vericar_senha(self, senha):
        return sha256.verify(senha, self.senha)