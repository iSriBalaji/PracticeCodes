from matplotlib import pyplot as plt
plt.style.use('ggplot')      #diff types of stylings available in matplotlib.
#plt.style.use('fivethirtyeight')
#plt.style.use('dark_background')
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="COVID-19",color='#355C7D',width=.25)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Meningitis", color='#CC2A49',width=.25)
plt.bar([.50,1.50,2.50,3.500,4.50],[70,30,60,40,45],
label="Pneumonia", color='#007788',width=.25)
plt.legend() #legend is the label which contains all info about the graph
plt.xlabel('Disease')
plt.ylabel('No of Patients(n)')
plt.title('MEDILAB Analytics - Types of diseases Vs No of Patients')
plt.tight_layout() #adjusts the plot into the given figure area
plt.show()
