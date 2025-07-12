agenda= list()
def inserir_pessoa():
    pessoa=dict()
    endereco=dict()
    telefone=dict()
    aniversario = dict()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['email']= str(input('E-mail: '))
    endereco['rua']=str(input('Rua: '))
    endereco['numero']= str(input('Numero: '))
    endereco['complemento'] = str(input('Complemento: '))
    endereco['bairro']=str(input('Bairro: '))
    endereco['cep'] = str(input('CEP: '))
    endereco['cidade'] = str(input('Cidade: '))
    endereco['estado'] =str(input('Estado: '))
    endereco['pais'] = str(input('Pais: '))
    pessoa['endereco']=endereco
    telefone['ddd'] =str(input('DDD: '))
    telefone['numero'] = str(input('Telefone: '))
    pessoa['telefone'] = telefone
    aniversario['dia'] =int(input('Dia do nascimento: '))
    aniversario['mes'] = int(input('Mes do nascimento: '))
    aniversario['ano'] = int(input('Ano do nascimento: '))
    pessoa['aniversario'] = aniversario
    pessoa['observacao'] = str(input('Observacao: '))
    agenda.append(pessoa)
def busca_primeiro_nome():
    entrada = input("Primeiro nome:: ").strip().lower()

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
        mes_de_aniversario =pessoa['aniversario']['mes']
        if mes_de_aniversario ==mes:
            imprimir_todos_dados(pessoa)
def busca_dia_mes():
    dia = int(input('Dia de aniversario: '))
    mes = int(input('Mes de naniversario: '))
    for pessoa in agenda:
        if pessoa['aniversario']['dia']== dia and pessoa['aniversario']['mes']==mes:
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
            da
        elif opcao == "2":
            imprimir_todos_dados(pessoa)
        else:
            print('Opcao invalida')
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
        escolha = input("Opção: ")

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



