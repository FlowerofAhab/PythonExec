minutos = int(input('Digite em minutos quanto tempo o cliente gastou ao telefone: '))
if minutos < 200:
    print ('sua conta ficou abaixo de 200 minutos portanto será cobrado apenas 0,20 por minuto')
    valor1 = float (minutos*0.20)
    print (f'o valor total será de {valor1: .2f}')
else:
    if minutos <= 400:
        print ('sua conta ficou acima de 200 minutos e abaixo de 400 portanto será cobrado 0.18 por minuto')
        valor2 = float (minutos*0.18)
        print (f'R$ {valor2: .2f}')
    else:
        print ('sua conta ficou acima de 400 minutos portanto será cobrado 0.15 por minuto')
        valor3 = float (minutos*0.15)
        print (f'R$ {valor3: .2f}')
