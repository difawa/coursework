import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def f(theta):
    tan = math.sin(math.radians(theta))/math.cos(math.radians(theta))
    result = 1000*(tan**2) - 980*tan - 1000
    return result


def catat(x1, x2, x3, x4, x5, x6, x7, x8):
    outF.write('{},{},{},{},{},{},{},{}\n'.format(x1, x2, x3, x4, x5, x6, x7, x8))
    return


a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

while f(a)*f(b) > 0:
    print("Ganti nilai a dan b")
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))

open('tabel.csv', 'w')  # untuk overwrite
outF = open('tabel.csv', 'a')  # untuk append
outF.write('i,a,x_sol,b,f(a),f(x_sol),f(b),b-a\n')

i = 0
if f(a) == 0:
    catat(i, a, a, b, f(a), 0, f(b), b-a)
elif f(b) == 0:
    catat(i, a, b, b, f(a), 0, f(b), b-a)
else:  # f(a) * f(b) < 0
    m = (a+b)/2
    catat(i, a, m, b, f(a), f(m), f(b), b-a)
    while not(-0.0001 <= (a-b) <= 0.0001):  # bisection
        i += 1
        if f(a)*f(m) < 0:
            b = m
            m = (a+b)/2
            catat(i, a, m, b, f(a), f(m), f(b), b-a)
        elif f(b)*f(m) < 0:
            a = m
            m = (a+b)/2
            catat(i, a, m, b, f(a), f(m), f(b), b-a)
        else:  # f(m) == 0
            catat(i, a, m, b, f(a), f(m), f(b), b-a)
            break


outF.close()

df = pd.read_csv('tabel.csv')
print(df)
print("Diperoleh sudut tembakan {}° ± 0.0001°.".format(df.loc[i, 'x_sol']))
df.plot(kind='line', x='i', y=['a', 'x_sol', 'b'], xlabel='banyak iterasi', ylabel='sudut(°)')
plt.xticks(np.arange(min(df['i']), max(df['i'])+1, 1))
plt.yticks(np.arange(min(df['a']), max(df['b'])+1, 1))
plt.show()
