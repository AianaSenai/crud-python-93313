import os 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco de dados
DATABASE_URL = "sqlite:///funcionarios.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Definição da classe Funcionario
class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    setor = Column(String, nullable=False)
    funcao = Column(String, nullable=False)
    salario = Column(Integer, nullable=False)
    telefone = Column(String, nullable=False)

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

# Funções CRUD
def salvar_funcionarios(funcionario):
    session.add(funcionario)
    session.commit()

def listar_todos_funcinarios():
    return session.query(Funcionario).all()

def pesquisar_um_funcionario(cpf):
    return session.query(Funcionario).filter(Funcionario.cpf == cpf).first()

def atualizar_funcionario(cpf, novos_dados):
    funcionario = pesquisar_um_funcionario(cpf)
    if funcionario:
        for key, value in novos_dados.items():
            setattr(funcionario, key, value)
        session.commit()
        print("Dados do funcionário atualizados com sucesso!")
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario(cpf):
    funcionario = pesquisar_um_funcionario(cpf)
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print("Funcionário excluído com sucesso.")
    else:
        print("Funcionário não encontrado.")

# Menu do sistema 
def menu():
    while True:
        print("\n ======= RH System =======")
        print("1- Adicionar funcionários")
        print("2- Consultar um funcionário")
        print("3- Atualizar os dados de um funcionário")
        print("4- Excluir um funcionário")
        print("5- Listar todos os funcionários")
        print('0- Sair do sistema')

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cpf = input("CPF: ")
            setor = input("Setor: ")
            funcao = input("Função: ")
            salario = int(input("Salário: "))
            telefone = input("Telefone: ")
            funcionario = Funcionario(nome=nome, idade=idade, cpf=cpf, setor=setor, funcao=funcao, salario=salario, telefone=telefone)
            salvar_funcionarios(funcionario)
            print("Funcionário adicionado com sucesso.")
        
        elif escolha == '2':
            cpf = input("Digite o CPF do funcionário: ")
            funcionario = pesquisar_um_funcionario(cpf)
            if funcionario:
                print(f"Funcionário encontrado: Nome: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}, Função: {funcionario.funcao}")
            else:
                print("Funcionário não encontrado.")
        
        elif escolha == '3':
            cpf = input("Digite o CPF do funcionário a ser atualizado: ")
            novos_dados = {}
            novos_dados['nome'] = input("Novo nome (deixe em branco para não alterar): ") or None
            novos_dados['idade'] = input("Nova idade (deixe em branco para não alterar): ") or None
            novos_dados['setor'] = input("Novo setor (deixe em branco para não alterar): ") or None
            novos_dados['funcao'] = input("Nova função (deixe em branco para não alterar): ") or None
            novos_dados['salario'] = input("Novo salário (deixe em branco para não alterar): ") or None
            novos_dados['telefone'] = input("Novo telefone (deixe em branco para não alterar): ") or None

            # Removendo chaves com valor None
            novos_dados = {k: v for k, v in novos_dados.items() if v is not None}
            atualizar_funcionario(cpf, novos_dados)
        
        elif escolha == '4':
            cpf = input("Digite o CPF do funcionário a ser excluído: ")
            excluir_funcionario(cpf)
        
        elif escolha == '5':
            funcionarios = listar_todos_funcinarios()
            for f in funcionarios:
                print(f"Nome: {f.nome}, Idade: {f.idade}, CPF: {f.cpf}, Setor: {f.setor}, Função: {f.funcao}, Salário: {f.salario}, Telefone: {f.telefone}")

        elif escolha == '0':
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    menu()
