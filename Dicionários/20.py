#Faça um programa para simular uma agenda de telefones. Para cada pessoa devem-se ter os seguintes dados: Nome, E-mail, Endereço (contendo campos para Rua, número, complemento, bairro, cep, cidade, estado, país), Telefone (contendo campo para DDD e número), Data de aniversário (contendo campo para dia, mês, ano), Uma string para alguma observação especial. O programa deve:
#◦ Definir uma função para inserir uma pessoa: Cria uma nova pessoa e insere os dados definidos anteriormente.
#◦ Definir uma função para buscar por mês de aniversário: Imprime os dados de todas as pessoas que fazem aniversário nesse mês.
#◦ Definir uma função para buscar por dia e mês de aniversário: Imprime os dados de todas as pessoas que fazem aniversário nesse dia e mês.
#◦ Definir uma função para imprimir agenda com as opções:
   # ▪ Imprime nome, telefone e e-mail.
    #▪ Imprime todos os dados.
#◦ O programa deve ter um menu principal oferecendo as opções acima. O menu deve ser outra função. Caso a opção seja 0, o programa encerra
agenda= list()
def inserir_pessoa():
    pessoa=dict()
    endereco=dict()
    telefone=dict()
    nascimento = dict()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['email']= str(input('E-mail: '))
    endereco['rua']=str(input('Rua: '))
    endereco['numero']= int(input('Numero: '))
    endereco['complemento'] = str(input('Complemento: '))
    endereco['bairro']=str(input('Bairro: '))
    endereco['cep'] = str(input('CEP: '))
    endereco['cidade'] = str(input('Cidade: '))
    endereco['estado'] =str(input('Estado: '))
    endereco['pais'] = str(input('Pais: '))
    pessoa['endereco']=endereco
    telefone['ddd'] =int(input('DDD: '))
    telefone['numero'] = str(input('Telefone: '))
    pessoa['telefone'] = telefone
    nascimento['dia'] =int(input('Dia do nascimento: '))
    nascimento['mes'] = int(input('Mes do nascimento: '))
    nascimento['ano'] = int(input('Ano do nascimento: '))
    pessoa['nascimento'] = nascimento
    pessoa['observacao'] = str(input('Observacao: '))
    agenda.append(pessoa)
def busca_primeiro_nome():
    entrada = input("Primeiro nome: ").strip().lower()

    for pessoa in agenda:
        primeiro_nome = pessoa['nome'].split()[0].lower()
        igual = primeiro_nome == entrada
        comeca_com = True
        if len(entrada) > len(primeiro_nome):
            comeca_com = False
        else:
            for i in range(len(entrada)):
                if primeiro_nome[i] != entrada[i]:
                    comeca_com = False
                    break
        if igual or comeca_com:
            imprimir_todos_dados(pessoa)
def busca_mes():
    mes = int(input('Mes de nascimento: '))
    for pessoa in agenda:
        mes_de_aniversario =pessoa['nascimento']['mes']
        if mes_de_aniversario ==mes:
            imprimir_todos_dados(pessoa)
def busca_dia_mes():
    dia = int(input('Dia do nascimento: '))
    mes = int(input('Mes do nascimento: '))
    for pessoa in agenda:
        if pessoa['nascimento']['dia']== dia and pessoa['nascimento']['mes']==mes:
            imprimir_todos_dados(pessoa)
def imprime_agenda():
    print("1: Imprimir apenas nome, telefone e email")
    print("2: Imprimir todos os dados")
    opcao = input("Opcao: ")
    for pessoa in agenda:
        if opcao == "1":
            dados = {
                "nome": pessoa["nome"],
                "telefone": {
                    "ddd": pessoa["telefone"]["ddd"],
                    "numero": pessoa["telefone"]["numero"]
                },
                "email": pessoa["email"]
            }
            print(dados)
        elif opcao == "2":
            imprimir_todos_dados(pessoa)
        else:
            print('Opcao invalida')
            break
def imprimir_todos_dados(pessoa):
    print(pessoa)
def menu_principal():
    while True:
        print("1: Inserir uma pessoa")
        print("2: Buscar por primeiro nome")
        print("3: Buscar por mes de nascimento")
        print("4: Buscar por dia e mes de nascimento")
        print("5: Imprimir agenda")
        print("0: Sair")
        escolha = input("Opcao: ")

        if escolha == "1":
            inserir_pessoa()
        elif escolha == "2":
            busca_primeiro_nome()
        elif escolha == "3":
            busca_mes()
        elif escolha == "4":
            busca_dia_mes()
        elif escolha == "5":
            imprime_agenda()
        elif escolha == "0":
            break
        else:
            print('Opcao invalida')
menu_principal()



