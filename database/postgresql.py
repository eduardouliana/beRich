import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'lotofacil'

class PostgreSQL:
  def __init__(self):
    self.connection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

  def insert_possibilities(self, id, value):
    cur = self.connection.cursor()
    cur.execute("insert into possibilidades_15 (id, numeros) values (%s, %s)", (id, value))
    self.connection.commit()

  def __del__(self):
    self.connection.close()
