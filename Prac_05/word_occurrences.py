sentence = input("Please enter a sentence: ")

list_from_string = {}

words = sentence.split()

for word in words:
    frequency_of_word = list_from_string.get(word)
    list_from_string[word] = frequency_of_word + 1

words = list(list_from_string.keys())  # put keys into a list
words.sort()

for word in words:
    print("{:{}} : {}".format(word, 12, list_from_string[word]))

