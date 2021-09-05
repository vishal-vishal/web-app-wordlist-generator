import re  # import module

# User inputs
user_input = input("Enter file name : ") 
output_file = input("Enter output file name : ")

# Read file
f = open(user_input, "r")

# Create list
word_list = []

# Iterate the date and split it.
for i in f:
    words = re.split(' |,|:|]|}|!|<|>|{', i)
    for word in words:
        word = word.replace('"', "").replace('[', "").replace("/","")
        word = word.lower()
        word_list.append(word)

# print(len(word_list))

word_list = list(set(word_list))
print(f"Total words : {len(word_list)}")

# Create and write word list file.

with open(output_file,'a') as out_put:
    for word in word_list:
        if word.isalpha():
            print(word)
            out_put.write(f"{word}\n")
