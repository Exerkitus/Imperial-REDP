import csv

with open("./ConvectiveCoolingDesigns.csv", r) as file:
    CSVlines = csv.DictReader(file)

print(CSVlines)
