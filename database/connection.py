import sqlite3

def __createTableLotofacil(conn):
    # cursor = conn.cursor()
    # cursor.execute("SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'LOTOFACIL';")
    # if (len(cursor.fetchall()) == 0):
    conn.execute('''CREATE TABLE LOTOFACIL (
        id            NUMERIC(10) PRIMARY KEY NOT NULL,
        numbers       VARCHAR(100),
        sorted_at     DATETIME,
        sequences     VARCHAR(250),
        groups        VARCHAR(250),
        even_numbers  NUMERIC(2),
        odd_numbers   NUMERIC(2)
    );''')

def __createTableDrawn(conn):        
    # cursor = conn.cursor()
    # cursor.execute("SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'LOTOFACIL';")
    # if (len(cursor.fetchall()) == 0):
    conn.execute('''CREATE TABLE NUMBERS (
        number         NUMERIC(2) PRIMARY KEY NOT NULL,
        quantity_drawn NUMERIC(9)
    );''')

def __prepareDB(conn):
    __createTableLotofacil(conn)
    __createTableDrawn(conn)

def connectDB(path):
    conn = sqlite3.connect(path)
    __prepareDB(conn)
    return conn

def disconnect(path):
    print("Need to implement later...")