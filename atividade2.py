# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError. 

def divisao():
  while True:
    try:
      number1 = float(input('>>'))
      number2 = float(input('>>'))
      div = number1 / number2
      print(f'O resultado da divisão é igual á {div} .')
    except ZeroDivisionError as divisao:
      print(divisao)
    except ValueError as error:
         print(error)

divisao()
       
