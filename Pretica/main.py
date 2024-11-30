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
        busca = ler_inteiro("Digite o ID do aluno que deseja buscar: ") #busca um aluno por id e apresenta seus dados se existir
        encontrado = next((aluno for aluno in alunos if aluno["id"] == busca), None)
    
        if encontrado:
            print("Aluno encontrado:")
            print_aluno(encontrado)
        else:
            print(f"Nenhum aluno encontrado com o ID {busca}.")
        pass
    elif (opc == 4):
        imc_min = ler_real("Digite o valor mínimo do IMC para o filtro: ", pos=True) #exibe uma lista com todos os alunos filtrados por imc
        imc_max = ler_real("Digite o valor máximo do IMC para o filtro: ", pos=True)

        alunos_filtrados = [
            aluno for aluno in alunos 
            if imc_min <= imc(aluno["peso"], aluno["altura"]) <= imc_max
        ]

        if alunos_filtrados:
                print(f"Alunos com IMC entre {imc_min:.2f} e {imc_max:.2f}:")
                print_alunos(alunos_filtrados)
        else:
                print(f"Nenhum aluno encontrado com IMC entre {imc_min:.2f} e {imc_max:.2f}.")
        pass
    elif (opc == 5):
        salvar(alunos,id) #salva os dados e pergunta se deseja sair do programa
        break
    else:
        print("Opção inválida!")

    limpar_tela()