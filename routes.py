from flask import request, render_template
import re
from flask import current_app as app
from model import db, Gene, Sample1, Sample2
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
    return 'TOP'


@app.route('/submit')
def find_by_search_input():
    input_text = request.args['search']
    # input_text = 'rs367896724'
    sample1 = ''
    sample2 = ''
    if input_text.startswith('rs'):
        row = Gene.query.filter_by(id=input_text).first()

        if row is not None:

            sam1 = Sample1.query.filter_by(id=input_text).first()
            sam2 = Sample2.query.filter_by(id=input_text).first()
            if sam1 is not None:
                sample1 = sam1.sample1.split(":")[0]
            if sam1 is not None:
                sample2 = sam2.sample2.split(":")[0]
            my_dict = {1: row.as_dict(), 2: sample1, 3: sample2}

            return my_dict
        else:
            return ''
    elif re.match('^[0-9]{1,2} [0-9]+', input_text):
        input_parts = input_text.split(' ')
        row = Gene.query.filter_by(chrom=input_parts[0]).filter_by(pos=input_parts[1]).first()
        if row is not None:
            sam1 = Sample1.query.filter_by(chrom=input_parts[0]).filter_by(pos=input_parts[1]).first()
            sam2 = Sample2.query.filter_by(chrom=input_parts[0]).filter_by(pos=input_parts[1]).first()
            if sam1 is not None:
                sample1 = sam1.sample1.split(":")[0]
            if sam1 is not None:
                sample2 = sam2.sample2.split(":")[0]
            my_dict = {1: row.as_dict(), 2: sample1, 3: sample2}

            return my_dict
        else:
            return ''
    else:
        return ''

