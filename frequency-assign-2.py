m=raw_input("Enter a string")
d={}
for i in m:
    if i in d:
         d[i]=d[i]+1
    else:
         d[i]=1
print d
