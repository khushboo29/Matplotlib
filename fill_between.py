import panda as pd
from matplotlib import pyplot as plt 

data = pd.read("data.csv")
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
 
plt.plot(ages, dev_salaries, color="#444444", linestyle='--', label="All Devs")

plt.plot(ages, py_salaries, label="Python Devs")

overall_median = 51725

plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries), interpolate=True, alpha=0.25, label="Above Avg")

plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries <= dev_salaries), interpolate=True, alpha=0.25, label="Below Avg")

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()

