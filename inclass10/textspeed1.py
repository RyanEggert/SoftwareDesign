import re, string


textFl = open('fish.txt', 'r')
textToParse = textFl.read()
textFl.close()

# Remove puntuation:

noPunc = string.translate(textToParse, None, string.punctuation)

print noPunc

print re.split('\s', noPunc.lower())
