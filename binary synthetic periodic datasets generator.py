# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:25:13 2020

@author: Migailo Giuseppe
"""

import numpy as np
import pandas as pd
import string
import random

seed = 10 # random seed

num_blocks = 40 # number of blocks

num_transactions_per_block = 50 # number of transactions per block

k = 3 # number of features

np.random.seed(seed)

periodicity = np.random.randint(1,5,k) # array of the k sine functions to generate the k features

blokSize = 10 # jKarma's blokSize

temp_data = np.zeros((num_blocks * num_transactions_per_block, k))

data = np.zeros((num_blocks * num_transactions_per_block))
data = data.astype(str)

groud_truth = np.zeros((int(len(data)/blokSize)))

columns = ["" for x in range(k)]
for i in range(k):
    columns[i] = random.choice(string.ascii_uppercase)

c = 0
t = 0
s = np.zeros((num_blocks * num_transactions_per_block))
for i in range(num_blocks):
    for j in range(num_transactions_per_block):
        for l in range(len(periodicity)):
            if j % periodicity[l] == 1:
                temp_data[c][l] = 1
                t = t + 1
            else:
                temp_data[c][l] = 0
        s[c] = t
        t = 0
        c = c + 1
    periodicity = periodicity + np.random.randint(1,5,k)

print(s)

i = 0
for row in temp_data:
    temp_str = ""
    for c,col in enumerate(row):
        if col == 1:
            temp_str = temp_str + columns[c] + " "
    data[i] = temp_str.strip()
    i = i + 1


print(np.sum(s)/(num_blocks * num_transactions_per_block))

startblokSize = blokSize
for i in range(len(groud_truth)):
    if blokSize <= num_transactions_per_block:
        groud_truth[i] = 0
        blokSize = blokSize + startblokSize
    else:
        groud_truth[i] = 1
        blokSize = startblokSize + startblokSize

dataset = pd.DataFrame(data, columns=["Transactions"])

dataset['Timestamp'] = pd.date_range(start='1/2/2019 09:00:00', periods = len(dataset), freq = '10min')

dataset = dataset[['Timestamp' , "Transactions"]]

dataset.to_csv("dataset 5.csv", sep = ";", index = False, encoding = 'utf-8-sig')

np.savetxt("groudtruth", groud_truth, fmt='%1d')

print(dataset)