import pandas as pd
import numpy as np

df = pd.read_csv('dataset/categorical.csv', sep=',', header=0)
print(df.head())
m = int(input("Please enter the confidence m:\n"))
p = {}

targetColumnName = str(df.columns[-1])
targetClasses = df[targetColumnName].unique()


# Priori probability
for cl in targetClasses:
    cnt = 0
    for el in df.as_matrix(columns=[targetColumnName]):
        if(el[0] == cl):
            cnt += 1
    p[cl] = cnt/df.shape[0]


for i in range(df.columns.shape[0]-1):
    col = df.columns[i]
    print("Processing " + str(col))

    for var in df[str(col)].unique():
        for tc in targetClasses:
            cntTot = 0
            cntFav = 0
            for el in df.as_matrix(columns=[str(col), targetColumnName]):
                if el[1] == tc:
                    cntTot += 1
                    if el[0] == var:
                        cntFav += 1
            p[str(var) + "/" + tc] = (cntFav + m*p[tc])/(cntTot + m)

print(p)
features = {}
for i in range(df.columns.shape[0]-1):
    col = df.columns[i]
    features[str(col)] = input("Please enter the value for " + str(col) + "\n")

maxProb = 0
cl = None
for tc in targetClasses:
    cp = 1
    for i in range(df.columns.shape[0]-1):
        col = df.columns[i]
        cp *= p[features[col] + "/" + tc]
    cp *= p[tc]
    if(cp > maxProb):
        cl = tc
        maxProb = cp

print("Prediction is " + str(cl))
