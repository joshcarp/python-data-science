from collections import defaultdict as dd

def count_trigrams(document):
    """ count_trigrams takes a string and returns a dictionary of the counts 
    of trigrams within the document. """
    trigram = dd(float)
    for i in range(0, len(document)-2):
        trigram[document[i:i+3]] += 1
    return trigram