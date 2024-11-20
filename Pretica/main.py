from aluno import *
from entrada import *
from navegabilidade import *

#variáveis de controle dos dados na memória
id = 1
""" número do id de autoincremento
"""
alunos = []
""" lista de dicionários que armazena as abstrações de alunos
"""

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")

    #navegabilidade
    if (opc == 1):
       aluno = cadastrar(id) #função lê os dados de aluno e retorna um dicionário
       alunos.append(aluno) #dicionário é adicionado na lista de alunos
       id += 1
        pass
    elif (opc == 2):
       print_aluno(alunos) #função imprime todos os alunos em tela
    elif (opc == 3):
        #busca um aluno por id e apresenta seus dados se existir
        pass
    elif (opc == 4):
        #exibe uma lista com todos os alunos filtrados por imc
        pass
    elif (opc == 5):
       salvar(alunos,id) #salva os dados e pergunta se deseja sair do programa
        break
    else:
        print("Opção inválida!")

    limpar_tela()