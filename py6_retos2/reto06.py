import random
z = random.randint(1,120)
print('El número resultante fué : ',z);
if z < 10 :
  print('El número',z,'es menor que 10');
elif z > 10 and z < 50 :
  print('El número',z,'está en el intervalo entre 10 y 50');
elif z > 50 and z < 100 :
  print('El número',z,'está en el intervalo entre 50 y 100');
else :
  print('El número',z,'es mayor que 100');