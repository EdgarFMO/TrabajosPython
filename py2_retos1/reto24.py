y=input('Dime una palabra: ').lower()

if y==y[::-1]:
  print('Es un Palíndromo')
else:
  print('No es un Palíndromo')