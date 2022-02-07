from matplotlib import pyplot as plt
plt.style.use('ggplot')      #diff types of stylings available in matplotlib.
#plt.style.use('fivethirtyeight')
#plt.style.use('dark_background')
plt.bar(['OMR','Kodambakkam','Adayar','Nungambakkam','Mount Road'],[48,34,42,24,17],
label="Female",color='#355C7D',width=.25)
plt.bar(['OMR','Kodambakkam','Adayar','Nungambakkam','Mount Road'],[12,8,15,5,15],
label="Male", color='#CC2A49',width=.25)
#plt.bar(['Kodambakkam','OMR','Adayar','Nungambakkam','Mount Road'],[70,30,60,40,45],
#label="Hantavirus pulmonary syndrome", color='#007788',width=.25)
plt.legend() #legend is the label which contains all info about the graph
#plt.xlabel('')
plt.ylabel('No of Cases(n)')
plt.title('MEDILAB Analytics - Location Vs No of Men&Women Affected')
plt.tight_layout() #adjusts the plot into the given figure area
plt.show()
