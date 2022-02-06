a={1:10,2:20,3:30,4:40}
b={5:50,6:60,7:70,8:80}
c={}
for i in (a,b):
    c.update(i)
print(c)