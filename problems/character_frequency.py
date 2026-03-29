# Program 1: Character frequency
word = "banana nana"
word = word.replace(" ", "")

char_count = {}

for char in word:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

print(char_count)


# Program 2: Word frequency
sentence = "apple banana apple mango banana"
word_count = {}

for word in sentence.split():
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

print(word_count)