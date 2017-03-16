import json
from pprint import pprint

product = 0
matrixList = []
maxProd = 0

with open('Matrix.json') as data_file:
    data = json.load(data_file)
#pprint(data["data"][1])
numberOfRows = len(data["data"])
for rowIndex in xrange(0,len(data["data"])):
    #itereates between each row
    elementsInRow = len(data["data"][rowIndex])
    #gets how many elements are in each row
    if (elementsInRow != numberOfRows):
        #validity for nxn matrix
        print("Matrix is not nxn. Now exiting")
        #quits process if not nxn
        break
    for element in xrange(0, elementsInRow - 2):
        #calculates from left to right of elements in row. elementsInRow -2 to make sure the end does not
        #get calculated
        try: 
            product = (data["data"][rowIndex][element]* data["data"][rowIndex][element + 1] * data["data"][rowIndex][element + 2])
            #calulates the product of data["data"][i],data["data"][i+1],data["data"][i+2],
            if (product > maxProd):
                #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                matrixList = list()
                maxProd = product
                matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex][element + 1], data["data"][rowIndex][element + 2]))
        except:
            print("end of row")
    #print("end of row")
print(matrixList)
print(maxProd)