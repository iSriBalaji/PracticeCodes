import matplotlib.pyplot as plt
from matplotlib import style
plt.style.use('dark_background')
#plt.style.use('ggplot')
population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar',color='#2e856e',rwidth=0.8)
plt.xlabel('Age Groups')
plt.ylabel('Number of people(n)')
plt.title('MEDILAB Analytics - Pneumonia Infection rate by age(as of March,2020)')
plt.show()
