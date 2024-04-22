import seaborn as sns
import matplotlib.pyplot as plt
#loading datadet
df=sns.load_dataset("iris")
sns.pairplot(df,hue='species')#hue="species"
plt.show()