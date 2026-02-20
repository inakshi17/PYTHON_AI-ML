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
print("original Data-\n")
hp=pd.DataFrame(house)
print(hp)
print("\n")

#normalization
n1=np.array(hp["area"])
n2=np.array(hp["price(cr)"])
mean_n1=np.mean(n1)
mean_n2=np.mean(n2)
std_n1=np.std(n1)
std_n2=np.std(n2)
hp["area"] = ((hp["area"] - mean_n1) / (std_n1)).round(2)
hp["price(cr)"] = ((hp["price(cr)"] - mean_n2) / (std_n2)).round(2)
print("new Data-\n")
print(hp)
