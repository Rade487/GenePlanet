from flask import request, render_template
import re
from flask import current_app as app
from model import db, Gene
from utils.create_db import create_table_from_vcf


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/load')
def import_vcf_into_db():

    # PART 1
    create_table_from_vcf('vcf_example.csv', 'gene')
    sql_id_index = 'create index id_index on gene(id)'
    sql_chrom_pos_index = 'create index chrom_pos_index on gene(chrom,pos)'
    sql_primary_key_gene = 'ALTER TABLE gene ADD PRIMARY KEY (index)'
    db.engine.execute(sql_id_index)
    db.engine.execute(sql_chrom_pos_index)
    db.engine.execute(sql_primary_key_gene)

    # PART 2
    sql_primary_key_sample1 = 'ALTER TABLE sample1 ADD PRIMARY KEY (index)'
    sql_primary_key_sample2 = 'ALTER TABLE sample2 ADD PRIMARY KEY (index)'

    create_table_from_vcf('sample1.csv', 'sample1')
    create_table_from_vcf('sample2.csv', 'sample2')

    db.engine.execute(sql_primary_key_sample1)
    db.engine.execute(sql_primary_key_sample2)
    return 'Data loaded in db. Populated tables are gene, sample1 and sample2'


@app.route('/submit')
def find_by_search_input():
    input_text = request.args['search']
    if input_text.startswith('rs'):
        try:
            row = Gene.query.filter_by(id=input_text).first()
        finally:
            db.session.remove()
        if row is not None:
            return row.as_dict()
        else:
            return ''
    elif re.match('^[0-9]{1,2} [0-9]+', input_text):
        input_parts = input_text.split(' ')
        try:
            row = Gene.query.filter_by(chrom=input_parts[0]).filter_by(pos=input_parts[1]).first()
        finally:
            db.session.remove()
        if row is not None:
            return row.as_dict()
        else:
            return ''
    else:
        return ''
