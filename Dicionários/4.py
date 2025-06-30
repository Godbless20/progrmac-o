#Escreva um trecho de código para fazer a criação dos novos tipos de dados conforme solicitado abaixo:
#Data: composto de dia, mês e ano.
#Horário: composto de hora, minutos e segundos.
#Compromisso: composto de uma data, horário e texto que descreve o compromisso.
#Leia n compromissos. Crie uma função que, dadas duas datas, retorne se a primeira ocorre antes da segunda ou não. Crie outra função semelhante, mas para comparar horários. Mostre os compromissos em ordem de data e horário.
def oc_datas(dic, p_data):
    if dic['ano'] < p_data['ano']:
        return 1
    elif dic['ano'] > p_data['ano']:
        return -1
    else:
        if dic['mes'] < p_data['mes']:
            return 1
        elif dic['mes'] > p_data['mes']:
            return -1
        else:
            if dic['dia'] < p_data['dia']:
                return 1
            elif dic['dia'] > p_data['dia']:
                return -1
    return 0

def oc_horarios(dic, p_horario):
    if dic['hora'] < p_horario['hora']:
        return 1
    elif dic['hora'] > p_horario['hora']:
        return -1
    else:
        if dic['minuto'] < p_horario['minuto']:
            return 1
        elif dic['minuto'] > p_horario['minuto']:
            return -1
        else:
            if dic['segundo'] < p_horario['segundo']:
                return 1
            elif dic['segundo'] > p_horario['segundo']:
                return -1
    return 0

calendario = []
n_compromissos = int(input())

for i in range(n_compromissos):
    compromissos = {}
    datas = {'dia': int(input("Dia: ")), 'mes': int(input("Mes: ")), 'ano': int(input("Ano: "))}
    compromissos['data'] = datas
    horario = {'hora': int(input("Hora: ")), 'minuto': int(input("Minuto: ")), 'segundo': int(input("Segundo: "))}
    compromissos['horario'] = horario
    compromissos['descricao'] = input("Descricao: ")
    calendario.append(compromissos)

organizacao = []

while calendario:
    menor = calendario[0]
    for compromisso in calendario:
        resultado_data = oc_datas(compromisso['data'], menor['data'])
        if resultado_data == 1:
            menor = compromisso
        elif resultado_data == 0:
            if oc_horarios(compromisso['horario'], menor['horario']) == 1:
                menor = compromisso
    organizacao.append(menor)
    calendario.remove(menor)

for c in organizacao:
    print(c)
