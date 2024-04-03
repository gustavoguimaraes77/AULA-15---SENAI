# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

def inserir():
   while True:
      try:
         number = int(input('>>'))
         print('É um número inteiro.')
         break
      except ValueError as inserir:
          print(inserir)
  
inserir()