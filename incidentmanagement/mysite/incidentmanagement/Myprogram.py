import requests
import simplejson as json
import json as simplejson
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity, pairwise_kernels
import pandas as pd
import requests as reqs
item_id = input("Enter Incident Number: ")
description = input("Enter Incident Description: ")
if item_id != "":
        item_id = float(item_id)
url = 'https://llgziael6y8a4oq-db201909061307.adb.uk-london-1.oraclecloudapps.com/ords/ananth/servicenow/'
PARAMS = {'limit':500}
response = requests.get(url = url, params = PARAMS, headers={'Content-Type': 'application/json'})
x = response.json()
df_idf = pd.DataFrame(x['items'])
if description != "":
        item_id = float('100000')
        df_idf = df_idf.append({'description' : description , 'incident_number' : item_id, 'assigned_to' : 'Dummy', 'resolution' : 'Dummy'} , ignore_index=True)
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 1), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(df_idf['description'])
cosine_similarities = pairwise_kernels(tfidf_matrix, tfidf_matrix)
similar_indices = cosine_similarities[0].argsort()[:-100:-1]
results = {}
for idx, row in df_idf.iterrows():
        # linear-kernel Or pairwise-kernel
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], df_idf['incident_number'][i]) for i in similar_indices]
        results[row['incident_number']] = similar_items[1:]
    #function to get a Id from Incident number
def item(incident_number):
        return df_idf.loc[df_idf['incident_number'] == incident_number, 'incident_number'].tolist()[0]
def description(incident_number):
        return df_idf.loc[df_idf['incident_number'] == incident_number, 'description'].tolist()[0]
def resolution(incident_number):
        return df_idf.loc[df_idf['incident_number'] == incident_number, 'resolution'].tolist()[0]
def team(incident_number):
        return df_idf.loc[df_idf['incident_number'] == incident_number, 'assigned_to'].tolist()[0]
def recommend(item_id, num):
        tempList=[]
        print("Top " + str(num) + " Incidents similar to Incident:" + str(item(item_id)) + " and their resolutions are")
        print("-------")
        recs = results[item_id][:num]
        for rec in recs:
            #print("Incident: " + str(item(rec[1])) + " is " + str(rec[0]*100) +  " percent similar and the resolution is " + resolution(rec[1]))
            a= "Incident: " + str(item(rec[1])) + " is " + str(rec[0]*100) +  " percent similar and the resolution is " + resolution(rec[1]) + " Team Resolved:" + team(rec[1])
            tempList.append(a)
        return tempList
ResValue = recommend(item_id=item_id, num=5)
print(ResValue)