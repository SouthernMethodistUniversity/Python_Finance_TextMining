#!/usr/bin/env python

import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import os, sys

filename = sys.argv[1]

def read_function(filename):
    ll = []
    with open(filename) as f:
        contents = f.read()
    contents = contents.split('<FILENAME>')[1]
    s = BeautifulSoup(contents, "html.parser")
    f = s.find_all('p')
    if len(f)==0:
        f = s.find_all('div')

    for i in range(len(f)):
        tt = f[i].text
        if tt is not None:
            ll = np.append(ll,tt)
    result = " ".join(ll).replace(u'\xa0', u' ').replace(u'\n',u' ').replace(u'\t',u' ')
    result = " ".join(result.split())
    
    name = filename.split('/')[-1].split('_')[0]
    date = filename.split('/')[-1].split('_')[1].split('.')[0]
    
    print('Done: '+filename)
    
    return (name, date, result)

df =pd.DataFrame(columns=['Name','Date','Story'])

info = read_function(filename)

df = df.append({'Name':info[0],'Date':info[1],"Story":info[2]}, ignore_index=True)
    
df["Date"]=pd.to_datetime(df["Date"])

df['Name'] = df['Name'].apply(lambda x: x.split('/')[-1])

string = filename.split('/')[-1].split('.')[0]

df.to_csv('{}.csv'.format(string), index=False, encoding='utf8')