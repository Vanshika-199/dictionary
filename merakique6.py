dict1={"ball":"red","bat":4,"wicket":8,"ball":"green","bat":3}
temp = []
res = dict()
for key, item in dict1.items():
    if item not in temp:
        temp.append(item)
        res[key] = item
print(res)