def somafaturamento(lista):
    soma = 0
    for i in lista:
        soma+= i[1]
    return soma

lista = [['SP', 67836.43],['RJ',36678.66],['MG',29229.88],['ES',27165.48],['Outros',19849.53]]
soma = somafaturamento(lista)
for i in lista:
    print(i[0]+f" representa {i[1]/soma*100:.2f}%"+" do valor total da distribuidora")