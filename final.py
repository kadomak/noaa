"""
Created on Fri May 15 23:23:23 2020
@author: Kowe
"""
#Imports
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

class GUI(Frame):
    def __init__(self,master):
        self.master = master
        master.title("NOAA Employment Data by Region and Sector")
          
        #Creating frames
        self.frame = Frame(master)
        self.frame.pack()
        self.middleframe = Frame(self.frame)
        self.middleframe.pack(side=BOTTOM)
        self.bottomframe = Frame(master)
        self.bottomframe.pack(side=BOTTOM)
                
        #Creating Background
        master.geometry("650x750")
        self.img = PhotoImage(file =r"RegionalMap.png")
        self.backgroundLabel= Label(self.frame,image=self.img)
        self.backgroundLabel.pack(fill=X)
        
        #Creating Entry Options
        self.regionLabel = Label(self.frame, text = "Select Region: ")
        self.regionLabel.pack(side=LEFT)
        self.regionEntry = Entry(self.frame, width = 15)
        self.regionEntry.pack(side=LEFT, fill= X)
        self.regionGuide = StringVar()
        self.regionInfo = Label(self.frame, textvariable = self.regionGuide, wraplength = 250)
        self.regionGuide.set("1-West, 2-Gulf of Mexico, 3-Southeast, 4-Mid Atlantic 5-Northeast, 6-North Pacific, 7-Pacific, 8-Great Lakes" )
        self.regionInfo.pack(side= LEFT, expand = True)
     
        self.sectorLabel = Label(self.middleframe, text = "Select Sector: ")
        self.sectorLabel.pack(side = LEFT, expand = True)
        self.sectorEntry = Entry(self.middleframe, width = 15)
        self.sectorEntry.pack(side=LEFT)
        self.sectorGuide = StringVar()
        self.sectorInfo = Label(self.middleframe, textvariable = self.sectorGuide, wraplength = 510)
        self.sectorGuide.set("1-Marine Construction, 2-Living Resources, 3-Offshore Mineral Extraction, 4- Ship and Boat Building, 5- Tourism and Recreation, 6- Marine Transportation" )
        self.sectorInfo.pack(side=LEFT)
               
        #Getting results
        self.newWindow = None
        self.results = Button(self.bottomframe, text="Display Results", command= self.resultsWindow)
        self.results.pack(side=BOTTOM)
              
       
    def getGraph(self): #this function  opens the file, gets user data, picks relevant data, and creates a graph
        ##Opening file
        self.file = open('enow_sector_region.csv', mode = 'r') #opening the file
        self.data = np.recfromcsv(self.file, dtype =None, encoding = 'utf-8') #the data is one huge array
        ##Variables & IDs
        self.year =[]
        self.employment = []
        self.regionName=""
        self.sectorName=""
        self.regionID = self.regionEntry.get()
        self.sectorID = self.sectorEntry.get()
        for lines in self.data:
            if lines[2] == int(self.regionID) and lines[6] == int(self.sectorID): #if the id numbers match the region and sector id
                self.regionName = lines[3] #record the name of the region (e.g. West)
                self.sectorName =  lines[7] #record the name of the sector (e.g. Marine Construction)
                self.year.append(lines[5]) #adding the appropriate years
                self.employment.append(lines[9]) #adding the appropriate employment per year
        self.name = "NOAA Employment Levels per Region: "+ self.regionName + " and sector: " + self.sectorName
        fig, ax = plt.subplots() 
        ax.plot(self.year, self.employment) #plots year vs employment
        ax.set(xlabel='Year', ylabel='Employment',title=self.name) #titling the plot and axes
        ax.grid() #this gives gridlines and can be removed if desired
        fig.savefig("test.png",bbox_inches="tight") #saving the figure
   
    def resultsWindow(self): #generates the new window with the results
        self.getGraph() #generates the graph
        if self.newWindow is None:
            self.newWindow = Toplevel()
            self.img1 = PhotoImage(file ="test.png")
            self.label = Label(self.newWindow,image = self.img1)
            self.label.pack(fill= BOTH,expand=True)
            self.newWindow.mainloop()
        else:
            self.newWindow.destroy()
            self.newWindow = None
            self.resultsWindow()

#main program
root = Tk()
myGui = GUI(root)
root.mainloop()

    
    
    