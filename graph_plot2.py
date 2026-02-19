import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data",loc='left',color='red',size=20)
plt.xlabel("Average Pulse",color='red',size=15)
plt.ylabel("Calorie Burnage",color='green',size=15)
plt.grid(c="k",ls='-')

plt.plot(x, y)
plt.show()
