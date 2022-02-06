dict = {"first":"1","second": "2","third": "1","four": "5", "five":"5","six":"9","seven":"7"}
list =[]
for val in dict.items(): 
  if val in list: 
    continue 
  else:
    list.append(val)
print (list)