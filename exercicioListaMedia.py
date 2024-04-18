try:
    n = int(input("Digite o tamnho da lista: "))

    lista = list(range(n))
    soma = 0
    for i in range(n):
        valor = int(input("Digite os valores das notas: "))
        lista[i] = valor
        soma = sum(lista)
    media = soma / len(lista)
    print("A Media é :",media)

except ZeroDivisionError:
    print("Não há nada na lista.")