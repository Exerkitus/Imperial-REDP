import csv, numpy as np

dataCSVName = "ConvectiveCoolingDesigns"

def openCSV(fileName):
    with open("./" + fileName, "r") as file:
        propArray = np.array([i for i in csv.reader(file)])

    propArray[1:], propDict = (np.where(propArray[1:] == "", 0, propArray[1:])), {}
    for i in range(0,len(propArray[0])):
        propDict[propArray[0,i].strip()] = propArray[1:,i].astype(np.float)
        continue
    return propArray, propDict

def getLengths(propDict):
    WL, lRho, d, D, nArgon, nCoolant = propDict["WorkingLength"], propDict["LinearDensity"], propDict["TubeOD"], propDict["WorkingDiameter"], propDict["NumberArTraces"], propDict["NumberCoolantTraces"]

    totalTraces = nArgon + nCoolant
    minH = d / lRho
    avgN = (WL - d) / (minH * totalTraces)

    H = minH * totalTraces
    l = np.sqrt(H**2 + (np.pi * (D+d))**2) * avgN
    propDict["TubeLength"] = np.round(l, 2)
    propDict["NumberTurns"] = np.round(avgN, 2)
    return propDict

def mainCalculate(propDict):
    propDict = getLengths(propDict)
    ##--Add further functionality here
    return propDict

def makeExportable(propArray, propDict):
    for i in range(0,len(propArray[0,:])):
        key = propArray[0,i]
        newArr = propDict[key]
        propDict[key] = np.where(newArr == 0, "", newArr)
        propArray[1:,i] = propDict[key]
        continue
        propArray = propArray.tolist()
    return propArray

def exportToCSV(propArray, dataCSVName):
    with open("./"+dataCSVName, "w", newline='') as file:
        writer = csv.writer(file)
        for i in propArray:
            writer.writerow(i)
    return

def main():
    global dataCSVName
    if dataCSVName[-4:] != ".csv":
        dataCSVName += ".csv"
    propArray, propDict = openCSV(dataCSVName)
    propDict = mainCalculate(propDict)
    exportToCSV(makeExportable(propArray, propDict), dataCSVName)
    return

main()
