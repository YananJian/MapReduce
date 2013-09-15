#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys
import os

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def format_print(atc_date, atc_total):
    for atc, date_pv in atc_date.iteritems():
        for date, pv in date_pv.iteritems():
            print atc_total.get(atc), '\t', atc, '\t', date, ':', pv

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    atc_date = {}
    atc_total = {}
    fname = os.environ["map.input.file"]
    __date = fname.split('-')[1]
    for atc, group in groupby(data, itemgetter(0)):
        try:
            if atc_total.get(atc):
                atc_total[atc] += int(count)
            else:
                atc_total[atc] = int(count)
            
            if not atc_date.get(atc):
                atc_date[atc] = ""

            if atc_date[atc].get(__date):
                atc_date[atc][__date] += (int(count) for art, count in group)
            else:
                atc_date[atc][__date] = int(count)
        except ValueError:
            pass
    format_print(atc_date, atc_total)

if __name__ == "__main__":
    main()
