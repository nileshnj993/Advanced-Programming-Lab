
def capitalize(sentence):
    words = sentence.split(" ")
    capitalized_sentence=""
    for word in words:
        capitalized_sentence += word.capitalize()
        capitalized_sentence+=" "
       
    return capitalized_sentence

sentence = input('Enter sentence: ')
print(capitalize(sentence))