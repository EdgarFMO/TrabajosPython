def ciclo():

 mdo = int(input('Escriba la tabla de que número desea saber: '))
 mor = int(input('Escriba hasta que número quiere que se multiplique: '))
 mor2 = mor+1
 for i in range(1,mor2):
     resu=i*mdo
     print(mdo,'x',i,'=',resu)

ciclo()