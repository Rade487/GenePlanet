from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:elektro8@localhost/postgres'
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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def init(self, chrom, pos, ref, alt, format):
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.format = format


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/load')
def import_vcf_into_db():
    # df = read_vcf('/Users/danilodobras/Downloads/hg37variants1000g.vcf')
    # df.to_csv('vcf_example.csv', index=False)
    # df.to_sql(db, 'gene')

    df = pd.read_csv('vcf_example.csv')
    df.to_sql(name='gene', con='postgresql://postgres:elektro8@localhost/postgres', index=False)
    sql_id_index = 'create index id_index on gene(id)'
    sql_chrom_pos_index = 'create index chrom_pos_index on gene(chrom,pos)'
    db.engine.execute(sql_id_index)
    db.engine.execute(sql_chrom_pos_index)
    return 'TOP'


@app.route('/submit')
def find_by_search_input():
    input_text = request.args['search']
    # input_text = 'rs367896724'
    if input_text.startswith('rs'):
        row = Gene.query.filter_by(id=input_text).first()
        if row is not None:
            return row.as_dict()
        else:
            return ''
    elif re.match('^[0-9]{1,2} [0-9]+', input_text):
        input_parts = input_text.split(' ')
        row = Gene.query.filter_by(chrom=input_parts[0]).filter_by(pos=input_parts[1]).first()
        if row is not None:
            return row.as_dict()
        else:
            return ''
    else:
        return ''


if __name__ == '__main__':
    app.run()
