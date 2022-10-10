import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'lotofacil'

class PostgreSQL:
  def __init__(self):
    self.connection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

  def insert_possibilities(self, id, numbers):
    cur = self.connection.cursor()
    cur.execute("insert into sorteios_possiveis (id, numeros) values (%s, %s)", (id, numbers))
    self.connection.commit()

  def set_sorted(self, id_sorteio, id):
    cur = self.connection.cursor()
    cur.execute("update sorteios_possiveis set id_sorteio = %s where id = %s", (id_sorteio, id))
    self.connection.commit()

  def __del__(self):
    self.connection.close()
