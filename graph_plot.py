import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y1=x**2
y2=x**3
plt.scatter(x,y1,label="x^2")
plt.scatter(x,y2,label="x^3")
plt.legend()
plt.show()
