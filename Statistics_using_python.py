
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[47]:


np.random.binomial(115,0.5)


# In[18]:


np.random.binomial(1000000000,0.5)/1000000000


# In[19]:


a=np.random.binomial(20,0.5,10000)


# In[24]:


(a>=15).mean()


# # chance of tornado

# In[27]:


chance=.01


# In[28]:


np.random.binomial(10000,chance)


# In[34]:


x=tornado_chance=np.random.binomial(1,chance,1000000)
twoday_tornado=0
for i in range(1,len(x)-1):
    if (x[i]==1 and x[i-1]==1):
        twoday_tornado+=1
print ('{} number of two days tornado in {} years'.format(twoday_tornado,1000000/365))        


# In[62]:


s=np.random.uniform(-1,0,1000)
#print (s)
np.all(s>1)
np.all(s<1)


# In[55]:


import matplotlib.pyplot as plt


# In[66]:


count,bins,ignored=plt.hist(s,15,normed=True)
print (count)
print (bins)
print (ignored)


# In[57]:


plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')


# In[59]:


plt.show()


# In[67]:


x=np.random.normal(0.75)


# In[78]:


mu, sigma = 0, 0.1 # mean and standard deviation
n=np.random.normal(mu, sigma, 1000)


# In[84]:


a=np.random.normal(0.75,size=1000)
np.std(a)


# In[85]:


import scipy.stats as stats


# In[86]:


stats.kurtosis(a)


# In[87]:


stats.skew(a)


# # Chi squared distributions

# In[98]:


chi_squared=np.random.chisquare(2,size=1000)
stats.skew(chi_squared)


# In[99]:


chi_squared=np.random.chisquare(6,size=1000)
stats.skew(chi_squared)


# In[92]:


import matplotlib.pyplot as pyplot
pyplot.pie([1,2,3])
pyplot.show()


# In[101]:


df=pd.read_csv(r'C:\Users\Ashish\Desktop\Test\Grades\Grades.csv')


# In[102]:


len(df)


# In[104]:


df.head(5)


# In[107]:


early= df[df['assignment1_submission']<='2015-12-31']


# In[111]:


late= df[df['assignment1_submission']>'2015-12-31']


# In[112]:


len(early)


# In[113]:


len(late)


# In[117]:


early['assignment1_grade'].mean()


# In[118]:


early.mean()


# In[119]:


late['assignment1_grade'].mean()


# In[120]:


late.mean()


# In[122]:


from scipy import stats
stats.ttest_ind


# In[123]:


stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])


# In[124]:


stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])


# In[126]:


get_ipython().magic('pinfo stats.ttest_ind')

