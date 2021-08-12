ndelista = int(input('Escriba el numero para la lista :  '))
num = ndelista + 10;
print('El número escogido es: ',num)
dos = 2;
uno = 1; 
while num > 1 :

 #num = num % 2;

 if (num % dos) == 0 :
  num = num / 2;
 elif (num % uno) == 1 :
  num = ((num*3) + 1);
 print(num)
