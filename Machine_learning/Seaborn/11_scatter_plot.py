#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
#loading datadet
df=sns.load_dataset("iris")

sns.scatterplot(x='sepal_length',y='petal_width',data=df,hue='species',size='species')#size='species'
plt.show()