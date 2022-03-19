import matplotlib.pyplot as plt
import numpy as np

T = []
pd1 = []
pd2 = []
pd3 = []


with open("data.txt") as file:
    for line in file:
        
        b = file.readline().split()
        
        for x in b:
            T.append(int(x))
            pd1.append(int(x))
            pd2.append(int(x))
            pd3.append(int(x))
print('t =', T)
print()
print('PD1 =', pd1)
print()
print('PD2 =', pd2)
print()
print('PD3 =', pd3)