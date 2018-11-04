
# coding: utf-8

# In[40]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='RZG3O4FEL2KEWDXI', output_format='pandas', indexing_type='date')


# In[ ]:

# Get MSFT data

msft, msft_meta = ts.get_daily(symbol='MSFT', outputsize='compact')
msft.tail()


# In[80]:

# Plot MSFT data

msft['4. close'].plot()
plt.xlabel('Time')
plt.ylabel('MSFT')
msft_mean = np.mean(msft['4. close'])
plt.axhline(msft_mean)
plt.show()


# In[81]:

# Get TSLA data

tsla, tsla_meta = ts.get_daily(symbol='TSLA', outputsize='compact')
tsla.tail()


# In[83]:

# Plot TSLA data

tsla['4. close'].plot()
plt.xlabel('Time')
plt.ylabel('TSLA')
tsla_mean = np.mean(tsla['4. close'])
plt.axhline(tsla_mean)
plt.show()


# In[ ]:



