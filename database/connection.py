import sqlite3


def _create_table_lotofacil(conn):
  conn.execute('''CREATE TABLE LOTOFACIL (
    id            NUMERIC(10) PRIMARY KEY NOT NULL,
    numbers       VARCHAR(100),
    sorted_at     DATETIME,
    sequences     VARCHAR(250),
    groups        VARCHAR(250),
    even_numbers  NUMERIC(2),
    odd_numbers   NUMERIC(2)
  );''')

def _create_table_numbers(conn):
  conn.execute('''CREATE TABLE NUMBERS (
    number         NUMERIC(2) PRIMARY KEY NOT NULL,
    combinations   VARCHAR(512),
    quantity_drawn NUMERIC(9)
  );''')

def _create_table_combinations(conn):
  conn.execute('''CREATE TABLE COMBINATIONS (
    combination  VARCHAR(200),
    occurrences  NUMERIC(9),
    quantity     NUMERIC(2)
  );''')

def _prepare_db(conn):
  _create_table_lotofacil(conn)
  _create_table_numbers(conn)
  _create_table_combinations(conn)

def connect(path):
  conn = sqlite3.connect(path)
  _prepare_db(conn)
  return conn

def disconnect(path):
  print(f"Need to implement later... {path}")
