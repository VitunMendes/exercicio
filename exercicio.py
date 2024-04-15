import os
while True:


    operacao = input ('Qual operação (+, -, *, /)? ou \'Q\' para sair')
    if operacao == 'Q' or operacao == 'q':
        break
                      

    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':

         x = int(input('Digite o primeiro numero: '))

         y = int(input('Digite o segundo numero: '))   

    if operacao == '+':
            result = x + y

    elif operacao == '-':
            result = x - y

    elif operacao == '*':
            result = x * y

    elif operacao == '/':
            result = x / y

    else:
            print('Operação Invalida')

    print(result)

    input('Press Enter')
    os.system('cls')

else:
    print('Operação Invalida')
    input('Press Enter')
    os.system ('cls')                                                                      