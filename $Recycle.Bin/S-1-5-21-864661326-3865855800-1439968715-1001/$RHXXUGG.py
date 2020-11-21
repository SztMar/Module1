# `ex_01_conection_to_db.py`

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)
    
if __name__ == "__main__":

   create_task_sql = """
   --Insert task into table
   INSERT INTO tasks (project_id, nazwa, opis, status, start_date, end_date)
   VALUES(123, 
           "zrobić pierwszy rekord", 
           "nadpisać pierwszy rekord", 
           "zrobione", 
           "2020-05-08 00:00:00", 
           "2020-05-10 00:00:00"
   );
   """
   db_file = "database.db"

   if conn is not None:
       execute_sql(conn, create_tasks_sql)

