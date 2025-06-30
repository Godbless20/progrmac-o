#Faça um programa que gerencie o estoque de um mercado e:
#Crie e leia um vetor de 5 produtos, com os dados: código (inteiro), nome (máximo 15 letras), preço e quantidade.
#Leia um pedido, composto por um código de produto e a quantidade. Localize este código no vetor e, se houver quantidade suficiente para atender ao pedido integralmente, atualize o estoque e informe o usuário. Repita este processo até ler um código igual a zero. Se, por algum motivo não for possível atender ao pedido, mostre uma mensagem informando que é “Impossivel atender ao pedido, produto sem estoque suficiente” ou “Impossivel atender ao pedido, codigo nao encontrado”.
#A cada passo, antes de ler o código, imprima o estoque do mercado.
estoques=list()
for i in range(5):
    produto=dict()
    produto['codigo']=int(input())
    produto['nome'] = str(input())
    produto['preco']=float(input())
    produto['quantidade']=int(input())
    estoques.append(produto)
while True:
    for electro in estoques:
        print(electro)
    codigo = int(input())
    if codigo==0:
        break
    quantidade = int(input())
    achou = False
    for electro in estoques:
        if electro['codigo'] == codigo:
            achou=True
            if electro['quantidade']>=quantidade:
                electro['quantidade'] -=quantidade
            else:
                print('Impossivel atender ao pedido, produto sem estoque suficiente')
            break
    if not achou:
        print('Impossivel atender ao pedido, codigo nao encontrado')