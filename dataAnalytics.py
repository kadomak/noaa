# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:45:49 2020
@author: Kowe Kadoma

I've provided a static example of how the data can be read and organized. 
This should provide a step in the right direction. From my understanding this is
how the project works: in the GUI a user puts in the region id and sector id, and 
then the employment data and the year are displayed on a graph. 

Each line of the csv is broken up as: geoid,geoname,regionid,region,geoscale, etc... 
with geoid being the 0th index, geoname the 1st index, etc...
(in other words line[0] = geoid, line[1] = geoname, etc....)
The code iterates through the file and checks to see if the region id and sector id match.
If it does, it records the year and employment number and then plots the result
"""
##numpy allows for the data to be entered and matplotlib creates the graph
import numpy as np
import matplotlib.pyplot as plt


file = open('enow_sector_region.csv', mode = 'r') #opening the file
data = np.recfromcsv(file, dtype =None, encoding = 'utf-8') #the data is one huge array

#the variables for plotting are the year and employment
year =[]
employment = []

#going through the data line by line
for lines in data:
    if lines[2] == 1 and lines[6] == 1: #if the id numbers match the region and sector id
        regionName = lines[3] #record the name of the region (e.g. West)
        sectorName =  lines[7] #record the name of the sector (e.g. Marine Construction)
        year.append(lines[5]) #adding the appropriate years
        employment.append(lines[9]) #adding the appropriate employment per year
        
#determing the region name
name = "NOAA Employment Levels per Region: "+ regionName + " and sector: " + sectorName
fig, ax = plt.subplots() 
ax.plot(year, employment) #plots year vs employment

ax.set(xlabel='Year', ylabel='Employment',title=name) #titling the plot and axes
ax.grid() #this gives gridlines and can be removed if desired
fig.savefig("test.png") #saving the figure
plt.show() #displaying the figure

