# python-language
snippets from comp10001 data science workshop

This snippet is used to classify what language a text is by slicing up strings up into "trigramm"

## How does it work?
### Training

- Take a sentence in any particular language and slice it up into 3 letter slices:

"my name is josh" --> ["my ", "nam", " e i" "s j", "osh"] (this includes spaces)

and now do it for another language: 

"je m'appelle josh" --> ["je ", "m'a", "ppe", "lle", " jo", "sh"]

you do this for enough "training data" of random text in a language, then you've got a list of commonly appearing "trigrams" in any language.


### Testing
- Now When a different string is presented we can split it into trigrams and compare it to the similarity of what we've just created:

"my name is miriam" -->  ["my ", "nam" , "e i", "s m", "iri", "am"]

and through some math, we can compare this with our trigrams in out English and French training set:

Simplifying a bit, but we have 3 trigrams that are the same: "my ", "nam" , "e i" when comparing our unknown to out English training set, and 0 of the same trigrams in our French training set, so it's __probably__ going to be an english string

how to run this example:
`python main.py name.txt` to run the example of "my name is miriam"

or

`python main.py input.txt` for something that's more interesting
