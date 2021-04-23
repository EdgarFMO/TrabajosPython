def masa():

 x = float(input('Escriba su estatura en metros: '))
 y = int(input('Escriba su peso en kilogramos: '))
 masa = y/(x**2)
 if masa<18.5:
   print('Su indice de peso es ',masa,'. El indice de peso es menor al normal') 
 elif ((masa>18.5) and (masa<24.9)):
   print('Su indice de peso es ',masa,'. El indice de peso es normal') 
 elif ((masa>25.0) and (masa<29.9)):
   print('Su indice de peso es ',masa,'. El indice de peso es superior al normal') 
 elif masa>=30.0:
   print('Su indice de peso es ',masa,'. El indice de peso indica que tiene obesidad')

masa()