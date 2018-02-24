
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#numpy implementation of binomial distribution
np.random.binomial(115,0.5)
np.random.binomial(1000000000,0.5)/1000000000
a=np.random.binomial(20,0.5,10000)

(a>=15).mean()


# # chance of tornado
chance=.01
np.random.binomial(10000,chance)
x=tornado_chance=np.random.binomial(1,chance,1000000)
twoday_tornado=0
for i in range(1,len(x)-1):
    if (x[i]==1 and x[i-1]==1):
        twoday_tornado+=1
print ('{} number of two days tornado in {} years'.format(twoday_tornado,1000000/365))        
s=np.random.uniform(-1,0,1000)
#print (s)
np.all(s>1)
np.all(s<1)
count,bins,ignored=plt.hist(s,15,normed=True)
print (count)
print (bins)
print (ignored)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()
x=np.random.normal(0.75)

mu, sigma = 0, 0.1 # mean and standard deviation
n=np.random.normal(mu, sigma, 1000)
a=np.random.normal(0.75,size=1000)
np.std(a)
stats.kurtosis(a)
stats.skew(a)
# # Chi squared distributions
chi_squared=np.random.chisquare(2,size=1000)
stats.skew(chi_squared)
chi_squared=np.random.chisquare(6,size=1000)
stats.skew(chi_squared)

pyplot.pie([1,2,3])
pyplot.show()
df=pd.read_csv(r'C:\Users\Ashish\Desktop\Test\Grades\Grades.csv')
len(df)
df.head(5)
early= df[df['assignment1_submission']<='2015-12-31']
late= df[df['assignment1_submission']>'2015-12-31']
early['assignment1_grade'].mean()
early.mean()
late['assignment1_grade'].mean()
late.mean()
from scipy import stats
stats.ttest_ind
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])

get_ipython().magic('pinfo stats.ttest_ind')
