import pandas as pd
import numpy as np
from sql_etl import create_table, excel_import
#Library for Data validations.
from cerberus import Validator


class data_ingestion():
    def createtable():
        col_list = ['firstname VARCHAR(255)', 'lastname VARCHAR(255)']  # and so on
        create_table('my_table2',col_list);

    def validation():
        schema = {'name': {'type': 'string'}}
        v = Validator(schema)
        document = {'name': 'john doe'}
        if v.validate(document):
            print('data is valid')
        else:
            print('invalid data')

    def import_csv_pandas():
        csv_path = '/Users/reshmabanaganapalli/Documents/Python_projects/dota/test_player.csv'
        schema_name = 'dota'
        excel_import(csv_path, schema_name,'test_player')

if __name__ == '__main__':
    #data_ingestion.createtable()
    #data_ingestion.validation()
    data_ingestion.import_csv_pandas()




