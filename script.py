import os
import sys
import matplotlib.pyplot as plt
import numpy as np

INPUT_FOLDER="/Users/i314050/work/paul_phd/input"
SEPARATOR = os.path.sep

points = []

#This is an object to store the X / Y values
class Entry:
   xAxisValue = 0
   yAxisValue = 0

   def __init__(self, xAxis, yAxis):
      self.xAxisValue = xAxis
      self.yAxisValue = yAxis

   def toString(self):
      return "xAxis: " + str(self.xAxisValue) + " yAxis:" + str(self.yAxisValue)

   def debug(self):
      print(self.toString())

#This loads the files
def loadFiles():
   for filename in os.listdir(INPUT_FOLDER):
      if filename.endswith(".txt"):
         readFile(INPUT_FOLDER + SEPARATOR + filename)

#This reads the files
def readFile(filename):
   inputFile = open(filename, 'r')
   content = inputFile.readlines()
   print("Filename: " + filename + " length =" + str(len(content)))
   for line in content:
      data = line.split()
      try:
         entry = Entry(float(data[0]), float(data[1]))
         entry2 = Entry(float(data[2]), float(data[3]))
         points.append(entry)
         points.append(entry2)
      except ValueError:
        print("Invalid line found: ")
        print(" Filename: " + filename)
        print(" Line: " + line)
   print("Loaded - " + str(len(points)))
   inputFile.close()

#This handles actually plotting the graph
def plotGraph():
   print("Plotting graph: " +str(len(points)))
   xValues = []
   yValues = []
   for point in points:
      xValues.append(point.xAxisValue)
      yValues.append(point.yAxisValue)
   if len(xValues) != len(yValues):
      print("Number of X Values does not match Y Values. Exiting")
      sys.exit()

   print("XValue length: " + str(len(xValues)))
   print("YValue length: " + str(len(yValues)))
   numPyXValues = np.array(xValues)
   numPyYValues = np.array(yValues)

   colors = (0,0,0)
   area = np.pi*3
   plt.scatter(numPyXValues, numPyYValues, s=area, c=colors, alpha=0.5)
   plt.title('Scatter plot')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.show()

#This is the main method
if __name__ == '__main__':
   print("Running script. Input=" + INPUT_FOLDER)
   loadFiles()
   plotGraph()
