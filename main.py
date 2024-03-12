#sample data stored as datatsf.csv
#importing all the necessary libraries:

import pandas as pd
import matplotlib.pyplot as plt
import sys

data = pd.read_csv('datatsf.csv')

#plotting to analyse the trend

#linearly increasing data
#Y=mx+c

#m: slope of the line
#c: y intercept

def descent(m_curr, c_curr, data_pts, rate) :
  m_des = 0.0
  c_des = 0.0

  n = len(data_pts)


  for i in range(n) : #will iterate through the data, look at the decrese in m and c
    a = data_pts.iloc[i].Hours
    b = data_pts.iloc[i].Scores

    #with this
    m_des += (-2/n)* a*(b-(m_curr*a+c_curr))
    c_des += (-2/n)* (b-(m_curr*a+c_curr))

  #m and c will be updated by the rate of learning

  m = m_curr - m_des*rate
  c = c_curr - c_des*rate

  return m, c

m = 0.0
c = 0.0
l_rate = 0.0001
epochs = 1000

for i in range(epochs) :
  m, c = descent(m, c, data, l_rate)

print(m, c)

def marks_for_hrs(m, c):
  hrs = float(input("Please input hours: "))
  return m*hrs + c
  
print(marks_for_hrs(m, c))


plt.scatter(data.Hours, data.Scores, color= "red")
plt.plot(list(range(0, 10)), [m*x + c for x in range(0, 10)], color="blue")
plt.show()
