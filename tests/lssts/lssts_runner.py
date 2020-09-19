"""
large scale stripper test suite
"""
import csv
from pathlib import Path

from swaglyrics.cli import stripper

dataset = Path(__file__).parent / 'lssts_dataset.tsv'

with open(dataset.resolve(), newline='', encoding="utf-8") as csvfile:
    f = csv.reader(csvfile, delimiter="\t")
    for row in f:
        # print(row)
        assert stripper(row[0], row[1]) == row[2]
