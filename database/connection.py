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
        combinations   VARCHAR(512),
        quantity_drawn NUMERIC(9)
    );''')
    
def __createTableCombinations(conn):
    conn.execute('''CREATE TABLE COMBINATIONS (
        combination  VARCHAR(200),
        occurrences  NUMERIC(9),
        quantity     NUMERIC(2)
    );''')

def __prepareDB(conn):
    __createTableLotofacil(conn)
    __createTableDrawn(conn)
    __createTableCombinations(conn)

def connectDB(path):
    conn = sqlite3.connect(path)
    __prepareDB(conn)
    return conn

def disconnect(path):
    print("Need to implement later...")