# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:25:13 2020

@author: Asus
"""

import numpy as np
import pandas as pd
import string
import random

seed = 10 # seed random

num_blocks = 40 # numbero di blocchi

num_transactions_per_block = 50 # numero di transizioni per blocco

k = 3 # numero di classi (feature)

np.random.seed(seed)

periodicity = np.random.randint(1,5,k) # array dei coeficenti m della k funzioni seno per generare le k feature

#print(periodicity)

blokSize = 10 # blokSize di jKarma

temp_data = np.zeros((num_blocks * num_transactions_per_block, k))
#temp_data = temp_data.astype(str)

data = np.zeros((num_blocks * num_transactions_per_block))
data = data.astype(str)

groud_truth = np.zeros((int(len(data)/blokSize)))

columns = ["" for x in range(k)]
for i in range(k):
    columns[i] = random.choice(string.ascii_uppercase)

#print(columns)

c = 0
for i in range(num_blocks):
    for j in range(num_transactions_per_block):
        for l in range(len(periodicity)):
            if j % periodicity[l] == 1:
                temp_data[c][l] = 1
            else:
                temp_data[c][l] = 0
        c = c + 1
    periodicity = periodicity + np.random.randint(1,5,k)
    
#print(temp_data)

i = 0
for row in temp_data:
    temp_str = ""
    for c,col in enumerate(row):
        if col == 1:
             temp_str = temp_str + columns[c] + " "
    data[i] = temp_str.strip()
    i = i + 1

#data = [(d or '0') for d in data]

''' 
c = 0
for i in range(num_blocks):
    for j in range(num_transactions_per_block):
        temp_str = ""
        for l in range(len(periodicity)):
            if j % periodicity[l] == 1:
                temp_data[c][l] = columns[l] + '1'
            else:
                temp_data[c][l] = columns[l] + '0'
            temp_str = temp_str + temp_data[c][l] + " "
        data[c] = temp_str.strip()
        c = c + 1
    periodicity = periodicity + np.random.randint(1,5,k)
'''

startblokSize = blokSize
for i in range(len(groud_truth)):
    if blokSize <= num_transactions_per_block:
        groud_truth[i] = 0
        blokSize = blokSize + startblokSize
    else:
        groud_truth[i] = 1
        blokSize = startblokSize + startblokSize
        
#print(data)
#print(groud_truth)

dataset = pd.DataFrame(data, columns=["Transactions"])

dataset['Timestamp'] = pd.date_range(start='1/2/2019 09:00:00', periods = len(dataset), freq = '10min')

dataset = dataset[['Timestamp' , "Transactions"]]

dataset.to_csv("dataset.csv", sep = ";", index = False, encoding = 'utf-8-sig')

np.savetxt("groudtruth", groud_truth, fmt='%1d')

print(dataset)