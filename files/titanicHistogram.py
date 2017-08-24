'''
histogram_age_income.py 
reads data from the age_income_feb14.csv
and creates two histograms: the age distribution and the income 
distribution. The data are from U.S. Census Bureau's February 2014 
Current Population Survey. 

(c) 2014 Project Lead The Way
'''
import matplotlib.pyplot as plt

# A generic helper function for matplotlib.pyplot graphics
def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Georgia')
        item.set_fontsize(16)

###
# Get the income/age data from CSV
###
# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'titanic.csv')
datafile = open(filename,'r')
data = datafile.readlines()

####
# Transform the data from strings to signed integers
####
liveList=[]
deadList=[]

for line in data[2:]: # Omit 0, 1, 2 because _______
    _,survived,passengerClass,sex,age,_,_,_,fare,_,_ = line.split(',')

    # ___________ the age data
    print survived
    
    if(survived=="0"):
        deadList.append(round(float(fare),0))
        print "dead"
    else:
        liveList.append(round(float(fare),0))
        print "live"
    
    
    
    
    
          

###
# Create the histograms
###

# Histogram 1
fig_age, ax  = plt.subplots(1, 1)
a = ax.hist([liveList,deadList], color=('cyan',"red"), bins=range(0, 170, 10),stacked=True) 

#ax1.hist(x, n_bins, normed=1, histtype='bar', stacked=True)
#ax1.set_title('stacked bar')


ax.set_title('Survival Rate of Titanic Passengers by Price of Ticket Purchased \n Green=Survived Red=Dead')
ax.set_xlabel('Ticket Price Purchased ($)')
ax.set_ylabel('Total Passengers (# people)')
make_PLTW_style(ax)
fig_age.show()

