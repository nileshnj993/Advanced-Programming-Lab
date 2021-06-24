a = [5,-5,5,-5,5,5]
a1=0
a2=0
for e in a:
    if(e%1==0):
        a1 = a1+e
        continue
    if(e%3==0):
        a2=a2+e
print(a1,end=" ")
print(a2)