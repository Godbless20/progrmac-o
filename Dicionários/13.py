#Peça ao usuário para digitar seus dados pessoais (Nome, Endereço, Data de Nascimento, Cidade, CEP, email), verifique se as informações de Data de Nascimento, CEP e email fazem sentido, e mostre ao usuário as informações, se estão todas corretas, ou mostre que alguma informação estava errada.
#For example:
def checa_data(nascimento):
    if len(nascimento) != 10:
        return False
    if nascimento[2] != '/' or nascimento[5] != '/':
        return False
    dia = nascimento[0:2]
    mes = nascimento[3:5]
    ano = nascimento[6:10]
    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
        return False
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1900 or ano > 2100:
        return False
    return True
def limpa_cep(cep):
    numeros = ""
    i = 0
    while i < len(cep):
        if '0' <= cep[i] <= '9':
            numeros += cep[i]
        i += 1
    return numeros
def checa_cep(cep):
    if len(cep) != 10:
        return False
    if cep[2] != '.' or cep[6] != '-':
        return False
    for i in range(10):
        if i == 2 or i == 6:
            continue
        if not ('0' <= cep[i] <= '9'):
            return False
    return True
def checa_email(email):
    if len(email) == 0:
        return False
    if email[0] == '@':
        return False
    pos_arroba = -1
    pos_ponto = -1
    for i in range(len(email)):
        if email[i] == '@':
            pos_arroba = i
            break
    if pos_arroba == -1 or pos_arroba == 0 or pos_arroba == len(email) - 1:
        return False
    for i in range(pos_arroba + 1, len(email)):
        if email[i] == '.':
            pos_ponto = i
            break
    if pos_ponto == -1:
        return False
    if pos_ponto == pos_arroba + 1:
        return False
    if pos_ponto == len(email) - 1:
        return False
    return True
Usuario = {
    "nome" : input(),
    "endereco" :  input(),
    "nascimento" : input(),
    "cidade" : input(),
    "cep" : input(),
    "email" : input()
}

if not checa_data(Usuario["nascimento"]):
    print("Data errada")
elif not checa_cep(Usuario["cep"]):
    print("CEP errado")
elif not checa_email(Usuario["email"]):
    print("E-mail errado")
else:
    print(Usuario)