# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 08:03:06 2020

@author: Migailo Giuseppe
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

seed = 10 # random seed

num_blocks = 40 # number of blocks

num_transactions_per_block = 50 # number of transactions per block

k = 3 # # number of features

np.random.seed(seed)

periodicity = np.random.randint(1,5,k) # array of the k sine functions to generate the k features

blokSize = 10 # jKarma's blokSize

num_bins = int(((num_blocks * num_transactions_per_block)/3*k)) # numero di bins

temp_data = np.zeros((num_blocks * num_transactions_per_block, k))

c = 0
for i in range(num_blocks):
    for j in range(num_transactions_per_block):
        for l in range(len(periodicity)):
            temp_data[c][l] = np.sin(c/periodicity[l])
        c = c + 1
    periodicity = periodicity + np.random.randint(1,5,k)

discretizer = KBinsDiscretizer(n_bins=num_bins, encode='ordinal', strategy='uniform')
discretizer.fit(temp_data)

temp_data = discretizer.transform(temp_data)

temp_data = temp_data.astype(int)

data = np.zeros(len(temp_data))
data = data.astype(str)

i = 0
for row in temp_data:
    temp_str = ""
    for c,col in enumerate(row):
        temp_str = temp_str + str(col) + " "
    data[i] = temp_str.strip()
    i = i + 1

dataset = pd.DataFrame(data, columns=["Transactions"])

dataset['Timestamp'] = pd.date_range(start='1/2/2019 09:00:00', periods = len(dataset), freq = '10min')

dataset = dataset[['Timestamp' , "Transactions"]]

dataset.to_csv("dataset.csv", sep = ";", index = False, encoding = 'utf-8-sig')

print(dataset)