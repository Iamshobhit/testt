#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[68]:


gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,3),dpi = 900)

plt.plot(gas.Year,gas.France,'b.-',label= 'France')
plt.plot(gas.Year,gas.Germany,'r.-',label = 'Germany')
plt.plot(gas.Year,gas['South Korea'],'g.-',label = 'South Korea')
#another way to plot
# for i in gas:
#     if i != 'Year':
#         plt.plot(gas.Year,gas[i],marker = '.')
    
plt.title('Global Gas Prices',
          fontdict ={'fontname':'Times New Roman',
                     'fontsize':20,
                     'fontweight':'bold',
                     'style':'italic'})

plt.xlabel('Year',fontdict ={'fontname':'Times New Roman',
                     'fontsize':15,
                     'fontweight':'bold',
                     })
plt.ylabel('USD',fontdict ={'fontname':'Times New Roman',
                     'fontsize':15,
                     'fontweight':'bold',
                     })
plt.xticks(gas.Year[::3])

plt.savefig('gas_prices.png',dpi = 900)
plt.legend()
plt.show()


# In[7]:


gas


# In[ ]:




