def sumatoria_2(A,B):

  n=len(A)//2
  acumulador=0
  for i in range(n):
    d = (A[i+1])**2
    e = d+B[n+1]
    acumulador = acumulador + e
  print(acumulador)
  return(acumulador) 
A = [4,6,8]
B = [2,2,2]  
sumatoria_2(A,B)
   