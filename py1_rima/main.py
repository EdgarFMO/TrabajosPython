
archivo = open('palabras500.csv', encoding="utf-8")
lineas = archivo.readlines()
archivo.close

print(len(lineas))

#def rima(silaba):
  #for contador in lineas :
    #x = contador 
    #y = x[-3:]
    #if y == silaba:    
     #print(contador)
     #return silaba
#rima('an')

def rima(silaba):
  for i in lineas :
    y = i[-3:]
    while y<=500 :
      if y==silaba:
       return(y)
    print(y)     

rima('an')      

#def rima(silaba):
    #if abs(num) <= 1:
        #return 1
    
    #div = abs(num)-1
    #while  num%div != 0 :
        #div = div - 1
    #return div
        
#rima('an')