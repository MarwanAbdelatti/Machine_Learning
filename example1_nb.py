import numpy as np
#import matplotlib.pyplot as plt

X = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
Y = [1, 1, 1, 2, 2, 2]

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)

res = clf.predict([[-0.8, -1], [1, 3]])
print(res)