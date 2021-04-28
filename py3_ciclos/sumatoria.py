def sumatoria_2(A,B,C):

  n=len(A)
  acumulador=0
  for i in range(n):
    d = C[i]
    e = A[i]*B[i]
    f = e*d
    acumulador = acumulador + e
    resu = acumulador + (n**2)
  print(resu)  
  return(resu)
A = [4,6,8]
B = [2,2,2]  
C = [1,2,3]

sumatoria_2(A,B,C)
   