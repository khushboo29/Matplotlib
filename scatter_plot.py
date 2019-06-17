import panda as pd
from matplotlib import pyplot as plt 

plt.style.use('seaborn')

data = pd.read('data.csv')
likes = data['likes']
view_count = data['view_count']
ration = data['ratio']

plt.scatter(view_count, likes, s=sizes, c=ratio, cmap='summer', marker="X", edgecolor="black", linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View count')
plt.ylabel('Total likes')

plt.tight_layout()
plt.show()

