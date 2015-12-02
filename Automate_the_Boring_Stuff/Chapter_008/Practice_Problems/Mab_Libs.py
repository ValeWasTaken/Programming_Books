# Chapter 8: Mad Libs - Python 3.4

def mad_libs():
    """
    Reads text files and lets the user add their own text anywhere
    the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
    """
    filler = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
    answer = []
    
    file = open('sentence.txt', 'r')
    content = file.read().split()

    for word in content:
        if word.strip('.|!|?|,') in filler:
            answer.append(input('Enter a {0}: '.format(word)))
        else:
            answer.append(word)
    
    file = open('sentence.txt', 'w')
    file.write(' '.join(answer))
    file.close()
mad_libs()
