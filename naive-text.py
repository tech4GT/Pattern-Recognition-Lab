import pandas as pd
import numpy as np

df = pd.read_csv('dataset/words.csv', sep=',', header=0)
print(df)
p = {}

targetColumnName = str(df.columns[-1])
targetClasses = df[targetColumnName].unique()

counts = {}
for cl in targetClasses:
    counts[cl] = 0
    cnt = 0
    for el in df.as_matrix(columns=[targetColumnName]):
        if(el[0] == cl):
            cnt += 1
    p[cl] = cnt/df.shape[0]

for row in df.as_matrix():
    cl = row[row.shape[0]-1]
    for col in range(row.shape[0]-1):
        counts[cl] += row[col]

for cl in targetClasses:
    for col in list(df.columns):
        if(col != targetColumnName):
            Nk = 0
            for row in df.as_matrix(columns=[col, targetColumnName]):
                if(row[1] == cl):
                    Nk += row[0]
            p[col + "/" + cl] = (Nk+1)/(counts[cl]+df.columns.shape[0]-1)

inp = {}
for col in list(df.columns):
    if(col != targetColumnName):
        inp[col] = int(input("Please Enter the number of times " +
                             str(col) + " occurs\n"))
max = 0
rv = None
for cl in targetClasses:
    val = p[cl]
    for col in list(df.columns):
        if(col != targetColumnName and inp[col] > 0):
            val *= p[col + "/" + cl]
    if val > max:
        max = val
        rv = cl
print("The prediction is " + str(rv))
