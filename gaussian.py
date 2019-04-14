import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = int(input("Please enter the mean\n"))
variance = int(input("Please enter the variance\n"))
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()
