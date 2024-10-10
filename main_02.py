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

print("Solicitando dados para o usuario")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu e-mail: ")
inserir_senha = input("Digite seu nome: ")

usuario = Usuario(nome= inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()

usuario = Usuario(nome ="Maria", email="maria@gmail.com", senha="456")
session.add(usuario)
session.commit()

#Delete
print("\nExcluindo um usuario")
email_usuario = input("Informe o email do usuario pra ser excluido: ")

usuario = session.query(Usuario).filter_by(email = email_usuario).first
session.delete(usuario)
session.commit()
print("Usuario excluido com sucesso")

#Listando todos os usuários do banco de dados
print("\nExibindo todos os usuiários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

#Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#Update 
print("\nAtualizando dados do usuario")
usuario = session.query(Usuario).filter_

#Fechando conexão
sess00ion.close()