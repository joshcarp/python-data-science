from train_classifier import train_classifier
from score_document import score_document
from classify_doc import classify_doc
import sys

if __name__ == "__main__":
    s = open(sys.argv[1]).read()
    print(classify_doc(s))
