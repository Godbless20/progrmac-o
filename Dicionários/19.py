vetor = list()

for i in range(5):
    pessoa = dict()
    endereco = dict()
    pessoa['nome'] = input('Nome: ')
    endereco['rua'] = input('Rua: ')
    endereco['bairro'] = input('Bairro: ')
    endereco['cidade'] = input('Cidade: ')
    endereco['estado'] = input('Estado: ')
    endereco['cep'] = input('CEP: ')
    pessoa['endereco'] = endereco
    pessoa['salario'] = float(input('Salario: '))
    pessoa['identidade'] = str(input('Identidade: '))
    pessoa['cpf'] = input('CPF: ')
    pessoa['civil'] = input('Estado Civil: ')
    pessoa['telefone'] = input('Telefone: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = input('Sexo: ')
    vetor.append(pessoa)

pessoa_maior_idade = vetor[0]
for pessoa in vetor:
    if pessoa['idade'] > pessoa_maior_idade['idade']:
        pessoa_maior_idade = pessoa
print('Pessoa com maior idade:')
print(pessoa_maior_idade)

sexo_masculino = []
for p in vetor:
    if p['sexo']== 'Masculino':
        sexo_masculino.append(p)

print('Pessoas do sexo masculino:')
for p in sexo_masculino:
    print(p)

salario_maior = []
for p in vetor:
    if p['salario'] > 1000:
        salario_maior.append(p)
print('Pessoas com salario maior que 1000:')
for p in salario_maior:
    print(p)
identidade = input('Identidade: ')
for p in vetor:
    if p['identidade'] == identidade:
        print(p)
        break