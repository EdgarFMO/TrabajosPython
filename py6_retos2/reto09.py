x = int(input('Escriba el número del valor inicial: '))
y = int(input('Escriba el número del valor final: '))
z = int(input('Escriba el intervalo: '))
total=0 #inicializamos la suma a cero
for i in range(x,y,z):
  total+=i #la variable total actúa de acumulador
  print(i)
print('La suma es:',total)