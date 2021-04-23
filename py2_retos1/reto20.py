def año():

  x = int(input('Ingrese el año que quiere saber si es bisiesto: '))
  c=x%4
  print(c)
  d=x%100
  print(d)
  e=x%400
  print(e)
  if ((c == 0) and (d!=0)):  
    print('El año',x,'es bisiesto')
  elif e == 0 :
    print('El año',x,'es bisiesto')
  else:
    print('El año',x,'no es bisiesto')

año()
