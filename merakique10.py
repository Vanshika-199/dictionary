dict =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
i = 0
for item in dict:
    item_list = dict[item]
    count = len(item_list)
    i += count
print(i)

