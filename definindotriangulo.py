a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))
if a == b and b == c:
    print ('é um triango equilátero')
elif a + b < c or a + c < b or b + c < a:
    print ('não é um triangulo')
else:
    print ('Escaleno')
