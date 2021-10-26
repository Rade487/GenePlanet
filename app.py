from flask import Flask, request,render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import re



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://newuser:pass@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Gene(db.Model):
    tablename = 'gene'
    id = db.Column(db.String(100), primary_key="True")
    chrom = db.Column(db.String(200))
    pos = db.Column(db.Integer)
    ref = db.Column(db.String(100))
    alt = db.Column(db.String(100))
    format = db.Column(db.String(100))

    def init(self, chrom,  pos, ref, alt, info):
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.info = info

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

@app.route('/submit')
def find_by_search_input():
    #input_text = request.form['search']
    input_text = 'rs367896724'
    if input_text.startswith('rs'):
        row = Gene.query.filter_by(id=input_text).first()
        return render_template('index.html', data=row)
    elif re.match('[0-9] ', input_text):
        input_parts = input_text.split(' ')
        row = Gene.query.filter_by(chrom=input_parts[0]).filter_by(pos=input_parts[1]).first()
        return render_template('index.html', data=row)
    else:
        return 'Not matched'


if __name__ == '__main__':
    app.run()