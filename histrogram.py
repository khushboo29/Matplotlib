import panda as pd
from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

data = pd.read("data.csv")
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60]
median_age=25

plt.hist(ages, bins=bins, edgecolor='black', log=True)

plt.axvline(median_age, color="red", label="Age Median", linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.show()

