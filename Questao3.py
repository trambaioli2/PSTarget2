import json

'''
Não entendi muito bem a parte que pede pra usar o json ou xml disponível, por isso criei um json 
com os faturamentos diários de um mês de uma empresa fictícia, colocando sábados domingos e feriados
com faturamento 0.
Também não quis usar recursos como min() e max() para pegar os valores maximos e minimos de um vetor,
pois como é um desafio de programação achei mais justo criar as funções que fazem essa ação.
'''


def menorvalor(vetor): #retorna o menor faturamento e seu respectivo dia
    aux = vetor[0]
    indice = 2
    dia = 1
    for i in vetor[1:]:
        if i != 0 and i<aux:
            aux = i
            dia = indice
        indice += 1
    return dia, aux

def maiorvalor(vetor): #retorna o maior faturmento e seu respectivo dia
    aux = vetor[0]
    indice = 2
    dia = 1
    for i in vetor[1:]:
        if i>aux:
            aux = i
            dia = indice
        indice += 1
    return dia, aux

def calculaMedia(vetor): #calcula a média de faturamento excluindo os dias de faturamento 0
    cont = 0
    soma = 0
    for i in vetor:
        if i != 0:
            cont+=1
            soma+=i
    return soma/cont

def faturamentos(vetor):
    maiordia, maiorValor = maiorvalor(vetor)
    menordia, menorValor = menorvalor(vetor)
    media = calculaMedia(vetor)
    cont = 0
    for i in vetor:
        if i > media: cont+=1 #conta os dias com fat maior que a média
    print("O dia "+str(maiordia)+" teve o maior faturamento do mês no valor de "+str(maiorValor))
    print("O dia "+str(menordia)+" teve o menor faturamento do mês no valor de "+str(menorValor))
    print(str(cont)+" dias ultrapassaram o valor da média mensal de faturamento")    

with open('faturamento.json', 'r') as file:
    data = json.load(file)  # Carrega os dados do JSON
    faturamento = data['daily_revenue']  # Acessa o faturamento diário

fatlista = []
for i in faturamento:
    fatlista.append(list(i.values())[1]) #coloca apenas os faturamentos na lista

faturamentos(fatlista)