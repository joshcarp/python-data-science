from train_classifier import train_classifier
from score_document import score_document

# We train the classifier here
default_lang_counts = train_classifier('train.csv')

def classify_doc(document, lang_counts=default_lang_counts):
    d = score_document(document, default_lang_counts)
    ans = sorted(d.items(), key = lambda x:x[1], reverse = True)
    if abs(ans[0][1] - ans[1][1]) < 1e-10:
        return "English"
    return ans[0][0]

