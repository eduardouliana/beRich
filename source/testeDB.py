import sqlite3
import sys
import os.path
from typing import Sequence

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from source.core.utils import readFile

def connectDB():
    return sqlite3.connect('./test.db')

def createTable(conn):
    conn.execute('''CREATE TABLE bigData (
        id            NUMERIC (10)  PRIMARY KEY NOT NULL,
        numbers       VARCHAR (100),
        sorted_at     DATETIME,
        sequences     VARCHAR(250)
    );''')
    print("Table created successfully")

def cleanData(conn):
    conn.execute("Delete from BIGDATA;")
    conn.commit()

def insertData(conn):
    allDraws = readFile.read("./resource/allDraws.json")
    for draw, numbers in allDraws.items():
        conn.execute("INSERT INTO BIGDATA (ID, NUMBERS) VALUES (" + str(draw) + ", '" + str(numbers) + "')")
    conn.commit()

def loadData(conn):
    return conn.execute("SELECT ID, NUMBERS FROM BIGDATA")

def saveData(conn, id, data):
    conn.execute("UPDATE BIGDATA SET SEQUENCES = '" + str(data) + "' where id = " + str(id))    

#Transform string to list
def toList(str):
    return str.strip('][').split(', ')

def extractSequences(numberList):
    def register(first, last):
        if first == last:
            sequences.append([first])
        else:
            sequences.append([first, last])    

    first = int(numberList[0])
    last = int(numberList[0])
    sequences = []

    for x in range(len(numberList)):
        if (last + 1) == int(numberList[x]):
            last = int(numberList[x])
            if x == len(numberList) - 1:
                register(first, last)
        elif ((last + 1) - first) > 0:
            if (x > 0): # Skip first execution
                register(first, last)
            first = int(numberList[x])
            last = int(numberList[x])

    return sequences

connection = connectDB()

createTable(connection)

cleanData(connection)

insertData(connection)

rowList = loadData(connection)

for row in rowList:
    # transform to array
    numberList = toList(row[1])
    # get sequences os draw
    sequences = extractSequences(numberList)
    # save to table
    saveData(connection, row[0], sequences)
connection.commit()

connection.close()