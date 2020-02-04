

def histogram(source_text):

    with open(source_text, "r") as file:
        og_text = file.read()

    word_list = og_text.split()

    for index, word in enumerate(word_list):
            word_list[index] = word.rstrip("&#@+?/[]{}!:;*_-.,()<>'")


    histogram = []
    for word in word_list:
        if histogram == []:
            histogram.append([word, 1])
        else:
            for curr_hist_pos in range(0, len(histogram)+1):
                try:
                    if word == histogram[curr_hist_pos][0]:
                        histogram[curr_hist_pos][1] += 1
                        break
                    elif curr_hist_pos == len(histogram):
                        histogram.append([word, 1])
                    else:
                        continue
                except (IndexError):
                    histogram.append([word, 1])



    return histogram



def unique_words(histogram):

    return len(histogram)



def frequency(word, histogram):

    unique_words = 0
    count = 0
    word_index  =  0
    word_exist = False

    while count < len(histogram):
        if histogram[count][word_index] == word:
            print(word + ' found')
            freq = histogram[count][1]
            return freq
        else:
            print(histogram[count][0] + ' is not ' + word)
            count +=1


if __name__ == "__main__":
    source_text = "test.txt"

    histogram_one = histogram(source_text)
    print(histogram_one)
    num_uniq_words = unique_words(histogram_one)
    print(num_uniq_words)

    test_freq = frequency("A",histogram_one)

    print(test_freq)
