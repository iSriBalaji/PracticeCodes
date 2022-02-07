from matplotlib import pyplot as plt
from matplotlib import style
#plt.style.use('dark_background')
plt.style.use('ggplot')
x = [5,3,6,2,8,9,6]
y = [3,8,12,16,19,24,28]
x2 = [2,1,5,7,4,3,7]
y2 = [3,8,12,16,19,24,28]
plt.plot(y,x,color='#2e856e',label='January',linewidth=2.5)
plt.plot(y2,x2,color='#1261a0',label='February',linewidth=2.5)
plt.title('MEDILAB Analytics - Analysis of Two months')
plt.xlabel('Date')
plt.ylabel('No of Patients(n)')
plt.legend()
#plt.grid(True,color='k')
plt.show()
