from matplotlib import pyplot as plt 

#for hand drawing plotting
plt.xkcd()

#print available style in plot
print(plt.style.available)

#to use particular style
plt.style.use('fivethirtyeight')

dev_x = []
dev_y = []

#for line graph
plt.plot(dev_x, dev_y)

#nice way of doing
plt.plot(dev_x, dev_y, 'k--', label="all dev") 

plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='.', label="all dev")  #nice way of doing

plt.xlabel(" label for x")
plt.ylabel(" label for y")
plt.title("title for graph")

plt.legend(['first plot legend', 'second plot legend'])

#nice way of doing
plt.legend()

plt.grid(True)

plt.tight_layout() #for padding adjustment

plt.savefig('plot.png')  #save the graph in system programmtically

plt.show()