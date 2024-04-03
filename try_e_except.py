while True:
      try:
         number = int(input('>>'))
         if number > 1:
            x = 10
            div = x / number
            
      except ValueError:
         print('Digite um número inteiro.')
      except ZeroDivisionError:
         print('Não pode dividir por zero.')
      except TypeError:
         print('O tipo de dado não corresponde.')
      finally:
         print(div)