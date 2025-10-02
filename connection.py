# conectar com o banco de dados
# sqlite

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URI = "sqlite:///sgu_database.db"

# teste de conexao

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connetion = engine.connect()
    print("Conexão com o banco de dados realizada com sucesso!")

except Exception as e:
    print("Erro ao conectar com o banco de dados:", e)


Base = declarative_base()