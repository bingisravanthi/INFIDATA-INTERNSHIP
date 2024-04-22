#importing packages
import seaborn as sns#advanced visualization
import matplotlib.pyplot as plt#for basic visualization

#loading dataset
df=sns.load_dataset("iris")#loading the dataset
print(df)#displaying the dataset

#draw lineplot
sns.lineplot(x="sepal_length",y="sepal_width",data=df)
#setting the title using Matplotlib
plt.title('Lineplot on IRIS dataset')
plt.show()#displaying the plot