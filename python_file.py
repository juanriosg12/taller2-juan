import numpy as np 

mu = 2
sigma = 0.8
n=1500
vals = np.random.normal(loc=mu,scale=sigma, size=n)

print(vals)