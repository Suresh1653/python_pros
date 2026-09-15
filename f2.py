l1=[10,20,30,20,30,40]
l2=[]
for i in l1:
    if l1.count(i)>1 and i not in l2:
        l2=l2+[i]
print(l2)

