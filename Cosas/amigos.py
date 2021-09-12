total = (float(input("¿Cuantos digitos quieres escribir?: ")))
numero = 0
suma = 1
distancia = []
while suma <= total:
  cont = (float(input("Digite la distancia: ")))
  distancia = distancia + [cont]
  suma = suma + 1
  numero = numero + cont
suma_t = numero /total
i=0
recorrido = total - 1
while i <= recorrido:
  distancia[i] =distancia[i] - suma_t
  i=i+1
  #print(abs(distancia[i])
print(suma_t)
print(distancia)