import pandas as pd
from dotenv import load_dotenv
from os import environ, path
from __init__ import db

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


def create_table_from_vcf(csv_path, table_name):

    sql_drop = 'drop table if exists' + table_name
    db.engine.execute(sql_drop)
    df = pd.read_csv(csv_path)
    df.to_sql(name=table_name, con='postgresql://postgres:elektro8@localhost/postgres', index=True)
