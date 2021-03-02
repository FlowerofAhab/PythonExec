
valor1 = int(input('Escreva um número: '))
valor2 = int(input('Escreva outra número: '))
valor3 = int(input('Escreva mais um número: '))
if valor1 > valor2 and valor1 > valor3:
    print(f'O número {valor1} é maior')
if valor2 > valor1 and valor2 > valor3:
    print (f'O número {valor2} é maior')
if valor3 > valor2 and valor3 > valor1:
    print (f'O número {valor3} é maior')
