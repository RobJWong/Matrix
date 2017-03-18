import json
from pprint import pprint

product = 0
matrixList = []
maxProd = 0
errorFlag = False
sequenceNumber =11

with open('MatrixMain.json') as data_file:
    data = json.load(data_file)
#pprint(data["data"][1])
numberOfRows = len(data["data"])

#print(len(data["data"]))
###########use while loop to check for 0's to process faster
for rowIndex in xrange(0,len(data["data"])):
    print("this is rowIndex %d",rowIndex)
    #itereates between each row
    elementsInRow = len(data["data"][rowIndex])
    #gets how many elements are in each row
    if (elementsInRow != numberOfRows):
        #validity for nxn matrix
        print("Matrix is not nxn. Now exiting")
        #quits process if not nxn
        errorFlag = True
        break
    for element in xrange(0, elementsInRow - (sequenceNumber - 1)):
        #calculates from left to right of elements in row. elementsInRow -2 to make sure the end does not
        #get calculated
        try: 
            product = (data["data"][rowIndex][element]* data["data"][rowIndex][element + 1] * data["data"][rowIndex][element + 2])
            print((data["data"][rowIndex][element], data["data"][rowIndex][element + 1], data["data"][rowIndex][element + 2]))
            print(product)
            #calulates the product of data["data"][i],data["data"][i+1],data["data"][i+2],
            if (product > maxProd):
                #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                matrixList = list()
                maxProd = product
                matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex][element + 1], data["data"][rowIndex][element + 2]))
        except:
            errorFlag = True
        try:
        #calculates the column sequence
            product = (data["data"][rowIndex][element]* data["data"][rowIndex + 1][element] * data["data"][rowIndex + 2][element])
            print((data["data"][rowIndex][element], data["data"][rowIndex + 1][element], data["data"][rowIndex + 2][element]))
            print(product)
            if (product > maxProd):
                #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                matrixList = list()
                maxProd = product
                matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex + 1][element], data["data"][rowIndex + 2][element]))
        except:
            errorFlag = True
        try:
        #calculates the diagonal from top left to bottom right
            product = (data["data"][rowIndex][element]* data["data"][rowIndex + 1][element + 1] * data["data"][rowIndex + 2][element + 2])
            print((data["data"][rowIndex][element], data["data"][rowIndex + 1][element + 1], data["data"][rowIndex + 2][element + 2]))
            print(product)
            if (product > maxProd):
                #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                matrixList = list()
                maxProd = product
                matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex + 1][element + 1], data["data"][rowIndex + 2][element + 2]))
        except:
            errorFlag = True
        try:
        #calculates the diagonal from top right to bottom left
            if(element >= (sequenceNumber - 1)):
                product = (data["data"][rowIndex][element]* data["data"][rowIndex + 1][element - 1] * data["data"][rowIndex + 2][element - 2])
                print((data["data"][rowIndex][element], data["data"][rowIndex + 1][element - 1], data["data"][rowIndex + 2][element - 2]))
                print(product)
                if (product > maxProd):
                    #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                    matrixList = list()
                    maxProd = product
                    matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex + 1][element - 1], data["data"][rowIndex + 2][element - 2]))
        except:
            errorFlag = True
            
# while (errorFlag != True):
#     for rowIndex in xrange(0,len(data["data"]))
print(matrixList)
print(maxProd)