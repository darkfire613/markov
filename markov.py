# A quick and dirty implementation of a markov chain generator
# Gets the linguistic data from a provided file called "Codex"
# Owen Monsma
# 23 May 2015
# owen.monsma@icloud.com

import random

FILENAME = "codex"

# Functions

def load_file(filename):
    file = open(filename, "r")
    codex = file.read()
    codex = [word for word in codex.split(' ') if word != '']
    for word in codex:
        word.lstrip(' \t\n\r')
        print word
    return codex

# Indexes each word with a list of tuples w following word and probability
def process_words(codex):
    processed = {word:[] for word in codex}

    return processed

# Logic

codex = load_file(FILENAME)
process_words(codex)

# Load in file

# Analyze words in file--relational probability

# Output string based on random starting word
