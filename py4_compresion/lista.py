A = [2,3,4]
B = [3,6,5]

n = len(A)//2

x = sum(((A[i+1])**2*B[2*i])+B[n+i]for i in range (n))
print(x)