import pandas as pd
import json


with open('data.json', mode='r', encoding='utf-8')as data:
    data = data.read()
lst = json.loads(data)
df_lst = []
for i in lst:
    id = i['id']
    city = i['location']['address']['city']['name']
    if i['totalPrice'] == None: 
        value = None 
        curr = None
    else:
        value = i['totalPrice']['value']
        curr = i['totalPrice']['currency']
    df_lst.append([id, city, value, curr])
df = pd.DataFrame(df_lst)
print(df)