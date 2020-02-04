import random
import sys
from frequency import histogram

def total_weight(histogram):

    weight = 0
    for element in histogram:
        weight += element[1]
    return weight


def generate_random_word(source_text):

    histogram_sample = histogram(source_text)


    count = 0


    random_num = random.randint(0,int(total_weight(histogram_sample)))

    for element in histogram_sample:

        random_num = random_num-element[1]

        if random_num <= 0:
            generated_word = element[0]
            return generated_word
            break

        else:


            continue
















if __name__ == "__main__":
    file = sys.argv[1]

    random_word = generate_random_word(file)
    print(random_word)
