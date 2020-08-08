import csv, numpy as np

dataCSVName = "ConvectiveCoolingDesigns"

def openCSV(fileName):
    if fileName[-4:] != ".csv":
        fileName += ".csv"
    with open("./" + fileName, "r") as file:
        propArray = np.array([i for i in csv.reader(file)])[:,:-1]

    propArray[1:], propDict = (np.where(propArray[1:] == "", 0, propArray[1:])), {}
    for i in range(0,len(propArray[0])):
        propDict[propArray[0,i].strip()] = propArray[1:,i].astype(np.float)
    return propDict

def main():
    global dataCSVName
    propDict = openCSV(dataCSVName)
    print(propDict['OptionNumber'])
    return

main()
