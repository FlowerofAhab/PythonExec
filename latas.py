m2 = int(input('Digite a quantidade em metros quadrados: '))
if m2 % 54 == 0:
    latas = m2 // 54
else:
    latas =(m2 // 54) + 1
    preco = latas * 80
    print (f'o número de latas será {latas}')
    print (f'R$ {preco: .2f}')
    
