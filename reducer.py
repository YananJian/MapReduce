#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys
import os

def format_print(atc_date, atc_total):
    for atc, date_pv in atc_date.iteritems():
        for date, pv in date_pv.iteritems():
            print (atc_total.get(atc)+'\t'+ atc+'\t'+ date+ ':'+ str(pv))

def main():
    atc_date = {}
    atc_total = {}
    for line in sys.stdin:
        line = line.strip()
        tmp = line.split('\t')
        if len(tmp) > 2:
            atc = tmp[0]
            date = tmp[1]
            pv = int(tmp[2])
            if atc_total.get(atc):
                atc_total[atc] += int(pv)
            else:
                atc_total[atc] = int(pv)
            
            if not atc_date.get(atc):
                atc_date[atc] = {}

            if atc_date[atc].get(date):
                atc_date[atc][date] += int(pv)
            else:
                atc_date[atc][date] = int(pv)
    format_print(atc_date, atc_total)
if __name__ == "__main__":
    main()
