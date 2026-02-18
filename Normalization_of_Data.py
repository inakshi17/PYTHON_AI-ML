import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

house={'type of house ':["house","house","flat","house","flat","flat","house",
                         "flat","flat","house","flat","house","flat","house",
                         "house","house","flat","house","flat","house"],
       'size':["3BHK","2BHK","1BHK","4BHK","2BHK","2BHK","3BHK","1BHK","1BHK",
               "2BHK","5BHK","1BHK","4BHK","2BHK","1BHK","2BHK","1BHK","1BHK",
               "4BHK","1BHK"],
       'area':[2000,3000,4000,2000,6000,3000,3000,1000,4000,3000,
               9000,1000,3000,4000,4000,5000,3000,2000,5000,2000],
       'price(cr)':[0.7,0.5,0.45,0.64,0.35,0.39,0.7,0.27,0.32,0.33,
                    1,0.43,0.98,0.43,0.65,0.43,0.76,0.12,0.82,0.22]}
hp=pd.DataFrame(house)
print(hp)

#before Normalization
plt.scatter(hp["size"], hp["price(cr)"])
plt.xlabel("Size (BHK)")
plt.ylabel("Price (cr)")
plt.title("Size(BHK) and Price(cr){before normalized value}")
plt.grid(True)
plt.show()

plt.scatter(hp["size"], hp["area"])
plt.xlabel("Size (BHK)")
plt.ylabel("area (square foot)")
plt.title("Size(BHK) and area(square foot){before normilized value}")
plt.grid(True)
plt.show()

#after Normalization
maxa = max(hp["area"])
mina = min(hp["area"])
hp["area"] = (hp["area"] - mina) / (maxa - mina)
maxp=max(hp["price(cr)"])
minp=min(hp["price(cr)"])
hp["price(cr)"] = (hp["price(cr)"] - minp) / (maxp - minp)
print("\n new data set after normalized value:\n")
print(hp)

plt.scatter(hp["size"], hp["price(cr)"])
plt.xlabel("Size (BHK)")
plt.ylabel("Price (cr)")
plt.title("Size(BHK) and Price(cr){after normilized value}")
plt.grid(True)
plt.show()

plt.scatter(hp["size"], hp["area"])
plt.xlabel("Size (BHK)")
plt.ylabel("area (square foot)")
plt.title("Size(BHK) and area(square foot){after normilized value}")
plt.grid(True)
plt.show()

y=hp["price(cr)"]
x=(hp["size"])
plt.title("Size(BHK) and Price(cr){after normilized value")
plt.xlabel("size(BHK)")
plt.ylabel("price(cr)")
plt.plot(x,y)
plt.show()    
