import random
from flask import Flask
from sample import generate_random_word

app = Flask(__name__)
def create_sentence(word_num):
    word_list=[]

    for _ in range(word_num):

        word_list.append(generate_random_word('../Code/test.txt'))

    sentence = ""
    for word in word_list:
        sentence+=word+" "
    return sentence

@app.route('/')

def index():
    return create_sentence(7)

if __name__ == '__main__':

    app.run(debug=True)
