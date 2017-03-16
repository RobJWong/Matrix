import json
from pprint import pprint

with open('Matrix.json') as data_file:
    data = json.load(data_file)
pprint(data["data"][1])
#numberOfRows = len(data["data"])
for index in xrange(0,len(data["data"])):
    #counts
    for elements in (data["data"][index]):
#numberOfElements = len(data["data"][0])
        print (elements)
