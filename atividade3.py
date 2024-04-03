# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. 
# Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

def inserir():
    while True:
        lista = [10,3,56,891,1,6]
        try:
            i = int(input('>>'))
            indice = lista[i]
            print(indice)
        except IndexError as error:
            print(error)
        except ValueError as error2:
            print(error2)
        except TypeError as error3:
            print(error3)

inserir()
