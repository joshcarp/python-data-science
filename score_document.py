from count_trigrams import count_trigrams
from train_classifier import train_classifier
from collections import defaultdict
# We train the classifier here
default_lang_counts = train_classifier('train.csv')

def score_document(document, lang_counts=default_lang_counts):
    file = document
    lines = ''.join([line for line in file]) 
    ans = count_trigrams(lines)
    cross_product = defaultdict(float)
    for lan in lang_counts:
        for key in ans:
            cross_product[lan] += ans[key]*lang_counts[lan][key]
    return cross_product