import math


def ed(p1, p2):
    # returns the euclidian distance of 2 features

    if(len(p1) != len(p2)):
        return -1
    dist = 0
    for i in range(len(p1)):
        dist = dist + ((p2[i] - p1[i])*(p2[i] - p1[i]))
    dist = math.sqrt(dist)
    return dist


num_features = input("\nPlease Enter the number of features\n")
num_features = int(num_features)
num_train = input("\nPlease Enter the number of data points\n")
num_train = int(num_train)

data = []
classes = []
for i in range(num_train):
    data.append([])
    for j in range(num_features):
        data[len(data)-1].append(float(input("\n Enter the value of next feature\n")))
    classes.append(input("\nEnter Class for this pair\n"))

# print(data)
# print(classes)

test_point = []

for i in range(num_features):
    test_point.append(
        float(input("\nEnter the value of feature for test pair\n")))
# print(test_point)


k = int(input("\nPlease Enter the k value\n"))
# print(k)


""" Find Euclidian distance for all and sort """
dist = {}
for i in range(num_train):
    dist[(ed(data[i], test_point))] = i

dist = sorted(dist.items())
# print(dist)

# Keep k and discard the rest
dist = dist[:k]
foundMajority = False
mjClass = ""
classCounts = {}

while not foundMajority:
    """ Run our algorithm to find majority and if there are ties we decrease k and try again """

    # make class counts 0
    for i in range(len(dist)):
        classCounts[classes[dist[i][1]]] = 0
    for i in range(len(dist)):
        classCounts[classes[dist[i][1]]] += 1

    # print(classCounts)
    maxClassCount = 0

    for key, value in classCounts.items():
        if value > maxClassCount:
            maxClassCount = value
            mjClass = key
    for key, value in classCounts.items():
        if value == maxClassCount and key != mjClass:
            maxClassCount = 0
            break

    if maxClassCount == 0:
        dist.pop()
        classCounts = {}
    else:
        foundMajority = True

print(mjClass)
