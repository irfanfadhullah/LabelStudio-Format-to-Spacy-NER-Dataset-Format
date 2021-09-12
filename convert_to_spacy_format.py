import pandas as pd
df1 = pd.read_json('/path/result.json')
entities_fix=[]
for index in df1.iloc[:,0]:
  entities = []
  for index2 in index:
    end, labels, start, text = [],[],[],[]
    for index3 in index2['result']:
      # print(index3)
      value = index3['value']
      end.append(value['end']),labels.append(value['labels']),start.append(value['start']),text.append(value['text'])
    ent = []
    for (a, b, c, d) in zip(end, labels, start, text):
      ent.append((c,a,b[0]))
    entities.append({'entities':ent})
  entities_fix.extend(entities)


text = []
for data in df1.iloc[:,1]:
  text.append(data['content'])

dataset = []
for (data,ent) in zip(text, entities_fix):
  dataset.append((data, ent))
df1['spacy_format'] = dataset