from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import pylab as p
import numpy as np

start = dt(2012,1,1) # Staring date
end = dt (2014,12,31) # Ending date
data = DR("4162.KL",'yahoo',start,end) # Use DataReader to read the data from yahoo
print('3 years of daily data for 4162, BAT') # Header
print(data) # Show the downloaded data

# Plot the 5-day moving average for BAT
bat = DR("4162.KL",'yahoo',start,end)['Close'] # Use DataReader to read the close price
mov_avg = pd.rolling_mean(bat,5) # Use the builit in function in pandas to calculate the moving average
p.plot(mov_avg) # Plot the graph
# Label the title, y-axis and x-axis
p.title('5-day moving average plot for BAT from \n 1/1/2012 to 12/31/2014')
p.xlabel('Days')
p.ylabel('Stock price,$RM$')
p.show()

# Download daily data for FTSEKLCI
klci=DR("^KLSE",'yahoo',start,end)
print('FTSEKLCI closing index') # Header of the table
print(klci) 

# Compute correlation between BAT and KLCI
com = ["4162.KL","^KLSE"]
data1 = DR(com,'yahoo',start,end)['Close']
combine = p.array(data1) # Set the data become array
print('Stock price corresponding to index') # Print the header
print(combine) # Print the result
correlation=data1.corr() # Use the built in function to calculate the correlation
print('Correlation between BAT and FTSEKLCI  \n',correlation) # Show the result


