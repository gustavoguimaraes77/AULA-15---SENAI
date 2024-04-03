# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção caso digite uma letra no divisor. 

def multiplicacao():
    while True:
        try:
            number1 = float(input('>>'))
            number2 = float(input('>>'))
            mult = number1 * number2
            print(f'O resultado da multiplicação é igual á {mult}')
            break
        except ValueError as multiplicacao:
            print(multiplicacao)

multiplicacao()
        
   