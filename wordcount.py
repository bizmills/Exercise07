input_file = open("twain.txt")

#builds dictionary
word_count = {}
words_list = []

for line in input_file:
    line_words = line.rstrip().split(' ')
    words_list += line_words

for word in words_list:
    if not word in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
for word, count in word_count.iteritems():
    print word, count