import os
import matplotlib.pyplot as plt
import numpy as np
dirpath = os.path.dirname(os.path.abspath(__file__))

def exponential(x, a, b, c):
    return a * np.exp(-b * x) + c

x_data = list()
y1 = list()
y2 = list()
for i in range(1000000):
    x_data.append(i)
    value1 = exponential(i, -128390.42104270413, -0.00000015874774439859617, 128479.1002465980)
    #value1 = -128390.42104270413 * np.exp(-0.00000015874774439859617 * i) + 128479.1002465980
    y1.append(value1)
    value2 = 0.0000030003395083049023 *i +12.469816746017331
    y2.append(value2)



plt.figure(figsize=(5,3))
plt.plot(x_data, y1, color='purple')
plt.plot(x_data, y2, color='green')
plt.yscale('log')
plt.savefig(f'{dirpath}/quickplot.png', dpi=512)
