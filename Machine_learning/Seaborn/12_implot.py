#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
#loading datadet
df=sns.load_dataset("iris")
sns.lmplot(x='petal_length',y='petal_width',data=df)
plt.show()
