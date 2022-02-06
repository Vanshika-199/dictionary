my_dict = {'data1':100,'data2': -54,'data3': 247}
def returnSum(my_dict):
    list = []
    for i in my_dict:
        list.append(my_dict[i])
    final = sum(list)
    return final
print("Sum :", returnSum(my_dict))