"""
data.py : functions to read data from different sources
"""
import pandas as pd
import json
import csv
from typing import Iterable


def read_txt(fname: str) -> Iterable[str]:
    """
    read_txt : an iterator to read big files line by line
    """
    with open(fname, 'r') as f:
        for i, line in enumerate(f):
            yield i, line.strip()


def read_json(fname: str) -> str:
    """
    read_json : returns the contents of a json file
    """
    with open(fname, 'r') as f:
        return json.load(f)


def read_jsonl(fname: str) -> Iterable:
    """
    read_jsonl : jsonl has a json per line
    """
    print('Simple Text File')
    with open(fname, 'r') as f:
        for line in f:
            try:
                movie = json.loads(line)
                yield movie['title']
            except:
                pass


def read_csv(fname: str, with_header: bool=True) -> Iterable:
    """
    read_csv : reads a comma delimited file, first line are headers
    """
    with open(fname, 'r') as f:
        data_reader = csv.reader(f, delimiter=',')
        if with_header:
            header = next(data_reader)  # read next in the iterator
            for line in data_reader:
                item = {header[i]: value for i, value in enumerate(line)}
                yield item
        else:
            for line in data_reader:
                yield line


if __name__ == '__main__':

    print('\nSimple Text File')
    fname = r'data\some_file.txt'
    for i, line in read_txt(fname):
        print('line {}: {}'.format(i, line))

    fname = r'data\movie.json'
    movie = read_json(fname)
    print('\nJson->Text\n', movie)
    print('\nText->Json\n', json.dumps(movie, indent=4))

    print('\nMovies from the 90s (jsonl)')
    fname = r'data\movies-90s.jsonl'
    for title in read_jsonl(fname):
        print(title)

    print('\nCSV File')
    fname = r'data\data.csv'
    data = read_csv(fname)
    for line in data:
        print(line)
