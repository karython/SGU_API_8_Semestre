from passlib.hash import pbkdf2_sha256 as sha256

class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    # getter
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    #REVIEW - verificar se não vai causar algum erro na hora de criar a senha
    # criptografar a senha
    def gen_senha(self, senha):
        self.senha = sha256.hash(senha)

    # verificar a senha
    def vericar_senha(self, senha):
        return sha256.verify(senha, self.senha)