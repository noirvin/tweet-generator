import random
from flask import Flask
from sample import generate_random_word
from markov import MarkovChain

app = Flask(__name__)
def create_sentence(word_num):
    source_text = "Nietsche.txt"
    with open(source_text, "r") as file:
        og_text = file.read()

    word_list = og_text.split()

    for index, word in enumerate(word_list):
            word_list[index] = word.rstrip("&#@+?/[]{}!:;*_-.,()<>'")
    chain = MarkovChain(word_list)
    sentence_words =[]



    sentence = chain.walk(word_num)

    return sentence

@app.route('/')

def index():
    return create_sentence(12)

if __name__ == '__main__':

    app.run(debug=True)
