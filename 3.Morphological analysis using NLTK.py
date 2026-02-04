from nltk.stem import PorterStemmer

# Input sentence
sentence = "The children are playing happily"

# Tokenization
tokens = sentence.split()

# Create Porter Stemmer object
stemmer = PorterStemmer()

print("Word\t\tStem")
print("----------------------")

for word in tokens:
    w = word.lower()          # Convert to lowercase
    stem = stemmer.stem(w)    # Apply stemming
    print(w, "\t\t", stem)
