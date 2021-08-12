import matplotlib
import matplotlib.pyplot as plt

ndelista = int(input('Escriba el numero para la lista:  '))

num = ndelista + 10;
print('El número escogido más 10 es: ',num)
dos = 2;
resu = [];
while num > 1 :

 if (num % dos) == 0 :
  num = int(num / 2);
 elif (num % dos) == 1 :
  num = (num*3) + 1;
  
 resu.append(num)
print('La lista es: ',resu)

plt.plot([resu])
plt.show()