#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("iris")

df['species']=df['species'].map({'setosa':1,
                                 'versicolor':2,
                                 'virginica':2})
correlation=df.corr()#getting correlation matrix
#creating a plot of coorelation matrix as heatmap
sns.heatmap(correlation,cbar=True,
            annot=True,linewidths=0.5,
            cmap='Blues')#displaying plot
plt.show()
#positive correlation is represented as light
#negitive correlation is represented as dark

