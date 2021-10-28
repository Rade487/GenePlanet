import pandas as pd
from dotenv import load_dotenv
from os import environ, path
from gene_planet import db

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


def create_table_from_vcf(csv_path, table_name):
    df = pd.read_csv(csv_path)
    df.to_sql(name=table_name,
              con=db.engine,
              if_exists='replace')
