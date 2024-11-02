# Create a program that:

# Asks the user to input a sentence.
# Counts the frequency of each word in the sentence.
# Displays the words and their frequencies in alphabetical order.

sentence = input("Enter a sentence:")

freqMap = {}

for token in sentence.lower().split():
    freqMap[token] = freqMap.get(token, 0) + 1   


print("Word Frequencies:")

for key in sorted(freqMap.keys()):
    print(f"{key} : {freqMap[key]}")