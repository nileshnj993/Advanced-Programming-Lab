def countWords(sentence):
    dict = {}
    words = sentence.split(" ")
    count = 0
    for word in words:
        dict[word] = 0
    for word in words:
        dict[word] += 1
        count = count+1
    print(dict)
    return count

print('OUTPUT')
print('------')
print('Nilesh Jain - 180953226')
print("The total number of words are:",countWords("Hello there, this is Nilesh. Hello World!"))