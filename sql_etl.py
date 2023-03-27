'''
This is the librariry for adding Python-SQL functions
1. Connect: connect to postgresql
2. create_table
'''

import psycopg2
from config import config
from sqlalchemy import create_engine
import pandas as pd


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')


        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_table(table_name,col_list):
    conn = None
    try:
        # create statement
        create_sql = 'CREATE TABLE '+ table_name + ' (' + ', '.join(col_list) + ');'
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(create_sql)
        print(create_sql)
        print('Table '+ table_name + ' created in PostgreSQL')
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def excel_import(csv_path,schema_name,table_name):
    conn = None
    try:
        df = pd.read_csv(csv_path)
        engine = create_engine('postgresql+psycopg2://postgres:may01@localhost:5432/testproject')
        conn = engine.raw_connection()
        cur = conn.cursor()
        df.to_sql(name= table_name,schema=schema_name, con= engine)
        create_sql = 'select * from '+ table_name+ ' ;'
        cur.execute(create_sql)
        conn.commit()
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()
    create_table()
    excel_import()
