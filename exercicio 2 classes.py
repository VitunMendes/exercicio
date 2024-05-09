import os

class ULA(object):
  
    def soma (self,primeiro_valor,segundo_valor):
  
        return  primeiro_valor + segundo_valor
        
    def sub (self,primeiro_valor,segundo_valor):
        
        return  primeiro_valor - segundo_valor
         
    def mult (self,primeiro_valor,segundo_valor):  

        return  primeiro_valor * segundo_valor
 
    def div (self,primeiro_valor,segundo_valor):
        
        return  primeiro_valor / segundo_valor
    
    def op_and (self,primeiro_valor,segundo_valor):
        
        return  primeiro_valor & segundo_valor
    
    def op_or (self,primeiro_valor,segundo_valor):
        
        return  primeiro_valor | segundo_valor
    
    def op_Not (self,primeiro_valor):
        
        return  ~ primeiro_valor    

ULA_OBJ = ULA()
operacao = input ('Qual operação (+, -, *, /)? ou \'Q\' para sair')
if operacao == 'Q' or operacao == 'q':
        pass
                      

elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':

         x = float(input('Digite o primeiro numero: '))

         y = float(input('Digite o segundo numero: '))   

if operacao == '+':
        result = ULA_OBJ.soma(x,y)
        print(f"O resultado é: {result}")

elif operacao == '-':
        result = ULA_OBJ.sub(x,y)
        print(f"O resultado é: {result}")

elif operacao == '*':
        result = ULA_OBJ.mult(x,y)
        print(f"O resultado é: {result}")

elif operacao == '/':
        result = ULA_OBJ.div(x,y)
        print(f"O resultado é: {result}")

else:
        print('Operação Invalida')