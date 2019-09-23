sentence = input("Please enter a sentence: ")

list_from_string = {}

words = sentence.split()

for word in words:
    frequency_of_word = list_from_string.get(word)
    list_from_string[word] = frequency_of_word + 1

words = list(list_from_string.keys())  # put keys into a list
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, list_from_string[word]))

