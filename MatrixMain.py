import json
from pprint import pprint

product = 0
matrixList = []
maxProd = 0
errorFlag = False

with open('MatrixMain.json') as data_file:
    data = json.load(data_file)
numberOfRows = len(data["data"])

###########use while loop to check for 0's to process faster
for rowIndex in xrange(0,len(data["data"])):
    #itereates between each row
    elementsInRow = len(data["data"][rowIndex])
    #gets how many elements are in each row
    if (elementsInRow != numberOfRows):
        #validity for nxn matrix. exits if it isn't
        print("Matrix is not nxn. Now exiting")
        errorFlag = True
        break
    for element in xrange(0, elementsInRow):
        #calculates the product of the next 11 elements from left to right
        try: 
            product = (data["data"][rowIndex][element]* data["data"][rowIndex][element + 1] * data["data"][rowIndex][element + 2] *
                       data["data"][rowIndex][element + 3]* data["data"][rowIndex][element + 4] * data["data"][rowIndex][element + 5] *
                       data["data"][rowIndex][element + 6]* data["data"][rowIndex][element + 7] * data["data"][rowIndex][element + 8] *
                       data["data"][rowIndex][element + 9]* data["data"][rowIndex][element + 10])
            if (product > maxProd):
                #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                matrixList = list()
                maxProd = product
                matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex][element + 1], data["data"][rowIndex][element + 2],
                       data["data"][rowIndex][element + 3], data["data"][rowIndex][element + 4] , data["data"][rowIndex][element + 5] ,
                       data["data"][rowIndex][element + 6], data["data"][rowIndex][element + 7] , data["data"][rowIndex][element + 8] ,
                       data["data"][rowIndex][element + 9], data["data"][rowIndex][element + 10]))
        except:
            pass
        try:
        #calculates the column sequence
            product = (data["data"][rowIndex][element]* data["data"][rowIndex + 1][element] * data["data"][rowIndex + 2][element] *
                       data["data"][rowIndex + 3][element]* data["data"][rowIndex + 4][element] * data["data"][rowIndex + 5][element] *
                       data["data"][rowIndex + 6][element]* data["data"][rowIndex + 7][element] * data["data"][rowIndex + 8][element] *
                       data["data"][rowIndex + 9][element]* data["data"][rowIndex + 10][element])
            if (product > maxProd):
                #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                matrixList = list()
                maxProd = product
                matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex + 1][element], data["data"][rowIndex + 2][element],
                                   data["data"][rowIndex + 3][element], data["data"][rowIndex + 4][element], data["data"][rowIndex + 5][element],
                                   data["data"][rowIndex + 6][element], data["data"][rowIndex + 7][element], data["data"][rowIndex + 8][element],
                                   data["data"][rowIndex + 9][element], data["data"][rowIndex + 10][element]))
        except:
            pass
        try:
        #calculates the diagonal from top left to bottom right
            product = (data["data"][rowIndex][element]* data["data"][rowIndex + 1][element + 1] * data["data"][rowIndex + 2][element + 2] *
                       data["data"][rowIndex + 3][element + 3]* data["data"][rowIndex + 4][element + 4] * data["data"][rowIndex + 5][element + 5] *
                       data["data"][rowIndex + 6][element + 6]* data["data"][rowIndex + 7][element + 7] * data["data"][rowIndex + 8][element + 8] *
                       data["data"][rowIndex + 9][element + 9]* data["data"][rowIndex + 10][element + 10])
            if (product > maxProd):
                #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                matrixList = list()
                maxProd = product
                matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex + 1][element + 1], data["data"][rowIndex + 2][element + 2],
                                   data["data"][rowIndex][element + 3], data["data"][rowIndex + 4][element + 4], data["data"][rowIndex + 5][element + 5],
                                   data["data"][rowIndex][element + 6], data["data"][rowIndex + 7][element + 7], data["data"][rowIndex + 8][element + 8],
                                   data["data"][rowIndex][element + 9], data["data"][rowIndex + 10][element + 10]))
        except:
            pass
        try:
            if((element - 10) >= 0):
                #calculates the diagonal from top right to bottom left
                product = (data["data"][rowIndex][element]* data["data"][rowIndex + 1][element - 1] * data["data"][rowIndex + 2][element - 2] *
                           data["data"][rowIndex + 3][element - 3] * data["data"][rowIndex + 4][element - 4] * data["data"][rowIndex + 5][element - 5] *
                           data["data"][rowIndex + 6][element - 6] * data["data"][rowIndex + 7][element - 7] * data["data"][rowIndex + 8][element - 8] *
                           data["data"][rowIndex + 9][element - 9] * data["data"][rowIndex + 10][element - 10])
                if (product > maxProd):
                    #checks to see if product is bigger than previous product. if so, it saves the matrix and product
                    matrixList = list()
                    maxProd = product
                    matrixList.extend((data["data"][rowIndex][element], data["data"][rowIndex + 1][element - 1], data["data"][rowIndex + 2][element - 2],
                                       data["data"][rowIndex + 3][element - 3], data["data"][rowIndex + 4][element - 4], data["data"][rowIndex + 5][element - 5],
                                       data["data"][rowIndex + 6][element - 6], data["data"][rowIndex + 7][element - 7], data["data"][rowIndex + 8][element - 8],
                                       data["data"][rowIndex + 9][element - 9], data["data"][rowIndex + 10][element - 10]))
        except:
            pass
print(matrixList)
print(maxProd)