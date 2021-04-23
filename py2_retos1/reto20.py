def año():

  x = int(input('Ingrese el año que quiere saber si es biciesto: '))
  c=x%4
  print(c)
  d=x%100
  print(d)
  e=x%400
  print(e)
  if ((c == 0) and (d!=0)):  
    print('El año',x,'es biciesto')
  elif e == 0 :
    print('El año',x,'es biciesto')
  else:
    print('El año',x,'no es biciesto')

año()
