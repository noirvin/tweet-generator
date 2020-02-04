import random
import sys
def create_sentence(word_list, word_num):
    sentence=[]

    for _ in range(word_num):

        sentence.append(word_list[random.randint(0,len(word_list)-1)])

    return sentence





if __name__ == "__main__":

    with open("/usr/share/dict/words", "r") as file:
        word_num = sys.argv[1]
        word_num = int(word_num)
        word_list = file.read().splitlines()
        sentence = create_sentence(word_list, word_num)
        print(" ".join(sentence))
