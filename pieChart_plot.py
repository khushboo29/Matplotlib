from matplotlib import pyplot as plt 


#to use particular style
plt.style.use('fivethirtyeight')

slices = [10,20,30,40]
labels = ['label1', 'label2', 'label3', 'label4']
colors = ['blue' ,'red', 'green', 'yellow']
explode = [0, 0, 0.1, 0]

plt.pie(slices, labels=labels, colors=colors, 
        explode=explode, shadows=True, autopct='%1.1f%%',
        startangle=90, wedgeprops={'edgecolor':'black'})

plt.title("Most Popular Languages")

plt.tight_layout() #for padding adjustment

plt.show()

