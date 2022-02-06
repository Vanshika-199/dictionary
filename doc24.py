a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
res={}
for d in a:
    if d['item'] not in res:
        res[d['item']] = d['amount']
    else:
        res[d['item']] += d['amount'] 
print(res) 