def fibonacci(numero): #Função para testar se o número pertence à sequência
    fibo = [0, 1] #Lista que incia a sequência
    while True: #Laço para realizar os testes
        fibo.append(fibo[-2]+fibo[-1]) #Cria o próximo número da sequência somando as duas últimas posições da lista
        if numero in fibo: #Testa se o número passado como parâmetro está na lista
            return "O número pertence à sequencia de Fibonacci"
        elif fibo[-1]>numero: #Se o último número da lista é maior que o número informado então este número não pertence à sequência
            return "O número não pertence à sequencia de Fibonacci"

print(fibonacci(float(input()))) #Printa a resposta final chamando a função e passando como parâmetro o número informado pelo usuário
