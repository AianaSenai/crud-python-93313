#.txt
#banco de dados
#SQL - Linguagem de Consulta Estruturada
#SELECT * FROM CLIENTES
#nome, sobrenome ,idade
#ORM
#I/O
#I - input(entrada)
#O - output(saída)



import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#criando bando de dados.
Meu_banco = create_engine("sqlite:///meubanco.db")

#criando conexão com banco de dados.
Session = sessionmaker(bind=Meu_banco)
session = Session()

#criando tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("sena", String)    

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

#Criando tabela no banco de dados.
Base.metadata.create_all(bind=Meu_banco)

#Salvar no banco de dados.
os.system("cls || clear")

usuario = Usuario(nome ="Marta", email="marta@gmail.com", senha= "123")
session.add(usuario)
session.commit()

usuario = Usuario(nome ="Maria", email="maria@gmail.com", senha="456")
session.add(usuario)
session.commit()

#Listando todos os usuários do banco de dados
print("\nExibindo todos os usuiários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#Fechando conexão
session.close()