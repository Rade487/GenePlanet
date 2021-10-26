from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from vcf_reader import read_vcf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://newuser:pass@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/load')
def import_vcf_into_db():
    # df = read_vcf('/Users/danilodobras/Downloads/hg37variants1000g.vcf')
    # df.to_csv('vcf_example.csv', index=False)
    # df.to_sql(db, 'gene')

    df = pd.read_csv('vcf_example.csv')
    df.to_sql(name='gene', con='postgresql://newuser:pass@localhost/postgres')
    return 'TOP'

if __name__ == '__main__':
    app.run()