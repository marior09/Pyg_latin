print 'Welcome to Mario\'s pig latin translator!'
pyg = 'ay'


original = raw_input("Enter a word friend!: ")
if len(original) > 0 and original.isalpha():
    print 'Perfect!'
    word = original.lower()
    first = word[0]
    if "aeiou".find(first) != -1:
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:len(word)] + first + pyg
        print new_word
else:
    print "I said a word, no numbers!"












