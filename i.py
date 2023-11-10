import numpy as np
b = [1,0,0,1]

a = np.array(b)
a = a.reshape(2,2)
print(a)

d = {'Age':20,
     'height':1.7,
     'color': "black",     
     }

d['Age'] = 21
d['height'] = 1.8
d['color'] = 'white'

print(d)

import pandas as pd
import matplotlib.pyplot as plt

data = {'x': [1,2,3,4,5,6], 'y':[3,6,1,3,7,4]}

df = pd.DataFrame(data)
print(df)
plt.plot(df)
print(df.loc[[0,1]])

#import pandas as pd


#df = pd.read_csv('RUUUUI.csv')
#a = df.to_numpy()

#a = np.array(df).reshape(3,3)
#print(a)