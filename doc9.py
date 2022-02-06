list1 = ["one", "two", "three","four","five"]
list2= [1,2,3,4,5]  
res = {}
for key in list1:
    for item in list2:
        res[key] = item
        list2.remove(item)
        break
print (res)