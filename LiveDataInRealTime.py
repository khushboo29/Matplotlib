import random
import pandas as pd 
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')

    plt.tight_layout()

#1000 means 1 sec
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()

plt.show()