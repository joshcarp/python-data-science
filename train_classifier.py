from collections import defaultdict as dd
import csv
from count_trigrams import count_trigrams
from math import sqrt

def normalise(counts_dict):
    """ normalise takes a dictionary of trigram counts counts_dict and
    normalises it by it's length."""
    mag = sqrt(sum([x**2 for x in counts_dict.values()]))
    return dd(int, {key: value/mag for (key, value) in counts_dict.items()})

def train_classifier(training_set):
    """ train_classifier takes a csv filename training_set as a string and
    returns a dictionary of average trigram-counts per language. """
    file = open(training_set)
    file = csv.reader(file)
    data = [row for row in file]
    # file.split()
    ans = dd(dd)
    
    for row in data:
        # print(row[1:])
        ans[row[0]] = normalise(count_trigrams(row[1:][0]))
    return ans