d1 = {1:10,2:20}
d2 = {3:30,2:40}
d3 = dict(d1)
d3.update(d2) 
for i, j in d1.items():
    for x, y in d2.items():
        if i == x:
            d3[i]=(j+y)
d4=d3
d5={5:50,6:60}
d6=dict(d4)
d6.update(d5)
for m,n in d4.items():
    for p,q in d5.items():
        if m==p:
            d6[m]=(n+q)
print(d6)
            
