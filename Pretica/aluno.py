from entrada import *
import json

# função cadastrar aluno
def cadastrar(id:int):
    aluno = {} 
    aluno['id'] = id # Adiciona uma nova chave 'id' ao dicionário `aluno`
    aluno['nome'] = input("Nome do aluno: ") # Adiciona uma nova chave 'nome' ao dicionário `aluno`

    # sexo do aluno
    while True:
        sexo = input("sexo ('M' - Masculino 'F'- Feminino 'N' - Não-informar) : ")
        sexo = sexo.upper() 
        if sexo in ["M","F","N"]:
            aluno["sexo"] = sexo
            break
        else:
            print("Opção inválida digite novamente")
    
    aluno['peso'] = ler_real("Peso (Kg): ",pos=True)
    aluno['altura'] = ler_real("Altura (m):",pos=True)
    aluno['mensalidade'] = ler_real("Mensalidade: ",pos=True)

    print("Cadastro bem sucedido!\n")
    print_aluno(aluno)

    return aluno

def print_aluno(aluno:dict): # declara que aluno é um dicionario
    for chave in aluno:        
        print(f"{chave.capitalize()}: {aluno[chave]}") # exibe o valor da chave com a primeira letra em maiusculo

def print_alunos(alunos:list): # mastra para o usuario uma lista com os alunos
    print(f"Imprimindo {len(alunos)} cadastro(s) de alunos\n")
    
    for aluno in alunos:
        print_aluno(aluno)
        print("................")

def salvar(alunos:list,id:int):
    lista = [alunos,id]

    try:
        with open("Alunos.json","w") as esc:
            json.dump(lista,esc,indent=4,ensure_ascii=False)
            print("Dados salvos com sucesso")
    except:
        print("Ocorreu erro na escrita do arquivo")

def ler_dados():
    try:
        with open("Alunos.json","r") as ler:
            lista = json.load(ler)
            print("Dados lidos com sucesso")
            return lista
    except:
        print("Ocorreu erro na leitura do arquivos")
