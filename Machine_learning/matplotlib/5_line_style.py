import matplotlib.pyplot as plt
import numpy as np

x=np.array([6,0])
ypoints=np.array([0,10])

plt.plot(ypoints,linestyle="dotted",color='red')#linestyle
plt.show()

plt.plot(ypoints,linestyle="dashed",color='#ffcee0')
plt.show()

plt.plot(ypoints,ls="dashdot",lw=10)
plt.show()

plt.plot(ypoints,ls="solid")
plt.show()


