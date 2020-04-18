
import click
import glob
from io import StringIO
from datetime import datetime
import os
import pandas as pd
import subprocess

@click.command()
@click.option('--input', default='data/nychealth/coronavirus-data/tests-by-zcta.csv',
    help='CSV to accumulate git history from.')
@click.option('--output', default='data/accum-nychealth-tests-by-zcta.csv',
    help='The file to write accumulated data to.')
def accumulate_data(input, output):
    
    log = subprocess.check_output(['git', 'log', '--follow', os.path.basename(input)],
                                  cwd=os.path.dirname(input))
    lines = log.decode('utf-8').split('\n')
    commits = [to_commit_hash(line) for line in lines if line.startswith('commit ')]
    dates = [to_date(line) for line in lines if line.startswith('Date:')]

    repo_root = get_repo_root(input)
    relative_path = find_repo_relative_path(input)

    result = pd.DataFrame()
    for date, commit in zip(dates, commits):
        file_contents = subprocess.check_output(['git', 'show', commit + ':' + relative_path],
                                                cwd=repo_root).decode('utf-8')
        df = pd.read_csv(StringIO(file_contents))
        df['Timestamp'] = date
        result = pd.concat([result, df])
    result.drop(columns=['zcta_cum.perc_pos']).to_csv(output, index=False)
        

def to_commit_hash(line):
    return line.replace('commit ', '').strip()


def to_date(line):
    date = line.replace('Date:', '').strip()
    date = ' '.join(date.split(' ')[:-1])
    return date


def get_repo_root(input):
    input_dir = os.path.dirname(input)
    repo_root_dir = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'],
                                            cwd=input_dir)
    return repo_root_dir.decode('utf-8').strip()


def find_repo_relative_path(input):
    repo_root_dir = get_repo_root(input)
    _, file_extension = os.path.splitext(os.path.basename(input))
    for relative_path in glob.glob(os.path.join(repo_root_dir, '*' + file_extension)):
        if relative_path.endswith(os.path.basename(input)):
            return relative_path.replace(repo_root_dir + '/', '')
    return None


if __name__ == '__main__':
    accumulate_data()
