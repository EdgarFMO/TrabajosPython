#a = list(range(1,11))
i=0
res=[]
while i < 10 :
  i+=1
  res.append(i)

b = list(range(11,21))
res.extend(b)
print(res)