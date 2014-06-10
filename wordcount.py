input_file = open("sample.txt")

#builds dictionary
word_count = {}
words_list = []

for line in input_file:
    line_words = line.rstrip().split(' ')
    words_list += line_words
print words_list