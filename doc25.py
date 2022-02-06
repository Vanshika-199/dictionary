count = {"w":0,"3":0,"r":0,"e":0,"s":0,"o":0,"u":0,"c":0}
word = "w3resource"
for i in word:
    if i == "w":
        count['w'] = count['w']+1
    elif i == "3":
        count['3'] = count['3']+1
    elif i == "r":
        count['r'] = count['r']+1
    elif i == "e":
        count['e'] = count['e']+1
    elif i == "s":
        count['s'] = count['s']+1
    elif i == "o":
        count['o'] = count['o']+1
    elif i == "u":
        count['u'] = count['u']+1
    elif i == "c":
        count['c'] = count['c']+1
print (count)