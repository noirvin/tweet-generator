import sys
import random

def shuffle_1(words):
    shuffled_words = []
    for _ in range(len(words)):
        random_word = words[random.randint(0, len(words)-1)]
        shuffled_words.append(random_word)
        words.remove(random_word)
    return shuffled_words

if __name__ == "__main__":
    words = sys.argv[1:]

    shuffled_words = shuffle_1(words)

    print(shuffled_words)
