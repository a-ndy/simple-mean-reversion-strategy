
# coding: utf-8

# In[129]:

import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt


# In[127]:

# Date range
start = dt.datetime(2011, 1, 1)
end = dt.datetime(2017, 12, 31)

# Load data
df = pdr.DataReader(['DEXUSUK', 'DEXUSEU'], 'fred', start, end)
df.tail()


# In[117]:

# Plot US/UK data

plt.plot(df.DEXUSUK)
plt.xlabel('Time')
plt.ylabel('US/UK')
usuk = np.mean(df.DEXUSUK) # Calculate mean
plt.axhline(usuk) # Plot mean
plt.show()


# In[118]:

# Plot US/EU data

plt.plot(df.DEXUSEU)
plt.xlabel('Time')
plt.ylabel('US/EU')
useu = np.mean(df.DEXUSEU) # Calculate mean
plt.axhline(useu) # Plot mean
plt.show()

