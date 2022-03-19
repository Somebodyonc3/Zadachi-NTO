import matplotlib.pyplot as plt
import numpy as np

fin = open('', 'r')

t = []
pd1 = []
pd2 = []
pd3 = []

for line in fin:
	line = fin.readline()
	x, y, z, a = map(int, line.split())
	t.append(x)
	pd1.append(y)
	pd2.append(z)
	pd3.append(a)
print(t, pdq, pd2, pd3, sep='\n')