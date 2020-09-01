import csv

from swaglyrics.cli import stripper

with open("./lssts_dataset.tsv", newline='', encoding="utf-8") as csvfile:
    f = csv.reader(csvfile, delimiter="\t")
    for row in f:
        # print(row)
        assert stripper(row[0], row[1]) == row[2]
