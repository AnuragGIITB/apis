
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import requests
import pandas as pd

key = 'key'
cx = 'cx'

url = 'https://www.googleapis.com/customsearch/v1'
parameters = {'q': input('input your query:'),
		 'cx':cx,
		 'key':key,
            'num':10,
		 'siteSearch':input('site to search from:')
		 }

page = requests.request('GET', url, params=parameters)


results = json.loads(page.text)
#print(results)
#print(results.keys())
for x in results.keys():
    print(x)
    
#print([item['link'] for item in results['items']])

title = [item['title'] for item in results['items']]
snippet = [item['snippet'] for item in results['items']]
link = [item['link'] for item in results['items']]

for i,j,k in zip(title, snippet, link):
    print(i);print(j);print(k);
    print('\n\n\n')
'''

def process_search(results):
    link_list = [item["link"] for item in results["items"]]
    df = pd.DataFrame(link_list, columns=["link"])
    df['link'] = [item['link'] for item in results['items']]
    df["title"] = [item["title"] for item in results["items"]]
    df["snippet"] = [item["snippet"] for item in results["items"]]
    return df

df = process_search(results)

#print(df)

'''
