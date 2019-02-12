import csv
from array_api import Array
with open('data.csv', newline='') as csvfile:
    datareader=csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(datareader):
        print(f'{i}:{row[0]},{row[1]},{row[2]}')
        if(row[0]=="CREATE"):
            array = Array()
        elif(row[0]=="DEBUG"):
            Array.debug_print(array)
        elif(row[0]=="ADD"):
            Array.add(array, row[1])
        elif(row[0]=="SET"):
            Array.set(array, row[1], row[2])
        elif(row[0]=="GET"):
            Array.get(array, row[1])
        elif(row[0]=="INSERT"):
            Array.insert(array, row[1], row[2])
        elif(row[0]=="DELETE"):
            Array.delete(array, row[1])
        elif(row[0]=="SWAP"):
            Array.swap(array, row[1], row[2])