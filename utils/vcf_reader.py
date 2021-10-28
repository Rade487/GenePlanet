import io
import pandas as pd


def read_vcf(path, num_of_rows):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': str, 'ID': str, 'REF': str, 'ALT': str,
               'FORMAT': str},
        sep='\t',
        nrows=num_of_rows
    ).rename(columns={'#CHROM': 'CHROM'})


def convert_vcf_to_csv(data_frame):
    return data_frame.to_csv('test.csv', index=False)


def remove_space_from_csv(dataset):
    trim = lambda x: x.strip() if type(x) is str else x
    return dataset.applymap(trim)
