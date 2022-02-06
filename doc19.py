student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science'] },'id2': {'name': ['David'], 'class': ['V'],'subject_integration': ['english, math, science']},'id3': {'name': ['Sara'], 'class': ['V'],'subject_integration': ['english, math, science']},'id4': {'name': ['Surya'], 
'class': ['V'], 'subject_integration': ['english, math, science']}}
temp = []
res = dict()
for key, item in student_data.items():
    if item not in temp:
        temp.append(item)
        res[key] = item
print(temp)