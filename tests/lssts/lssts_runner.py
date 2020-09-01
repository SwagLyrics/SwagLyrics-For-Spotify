import csv
import os

from swaglyrics.cli import stripper

dataset = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lssts_dataset.tsv')

with open(dataset, newline='', encoding="utf-8") as csvfile:
    f = csv.reader(csvfile, delimiter="\t")
    for row in f:
        # print(row)
        assert stripper(row[0], row[1]) == row[2]
