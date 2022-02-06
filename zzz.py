a=input("enter the string: ")
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(str(b))


ayu={"name":"ayushi","age":21,"gender":"female"}
b=[(i,j)for i, j in ayu.items()]
print(b)

solve={"a":{"b":1,"c":{"e":21,"f":72}}}
for i in a:
    print(i)
    if type(a[i])==type({}):
        for j in a[i]:
            print(j)
            if type(a[i][j])==type({}):
                for k in a[i][j]:
                    print(k,a[i][j][k])
            else:
                print(j,a[i][j])
    else:
        print(i,a[i])

2