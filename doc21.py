data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
temp = []
res = dict()
for key, item in data.items():
    if item not in temp:
        temp.append(item)
        res[key] = item
print(res)

###doubt
