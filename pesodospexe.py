peso = int(input('Insira a quantidade em KG de peixes: '))
e = (peso-50)
if e < 0:
    print (' está dentro do limite, não terá multa')
else:
    multa = float (e*4.00)
    print (f' sua multa será de {multa}')
    
  
    

    
