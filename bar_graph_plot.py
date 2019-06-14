from matplotlib import pyplot as plt 
import numpy as np

#to use particular style
plt.style.use('fivethirtyeight')

ages_x = []

x_indexes = np.arrange(len(ages_x))

dev_y = []

#for bar graph
plt.bar(x_indexes, dev_y)

plt.bar(x_indexes - width, dev_y1, width='width', color='k', linestyle='--', marker='.', label="all dev")  #nice way of doing
plt.bar(x_indexes, dev_y2, width='width', color='k', linestyle='--', marker='.', label="python dev")  #nice way of doing
plt.bar(x_indexes + width, dev_y3, width='width', color='k', linestyle='--', marker='.', label="javascript dev")  #nice way of doing

plt.xticks(ticks='x_indexes', label='ages_x')

plt.xlabel(" label for x")
plt.ylabel(" label for y")
plt.title("title for graph")

#nice way of doing
plt.legend()

plt.grid(True)

plt.tight_layout() #for padding adjustment

plt.savefig('plot.png')  #save the graph in system programmtically

plt.show()