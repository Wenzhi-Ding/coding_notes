# https://stackoverflow.com/questions/73349913/how-can-i-replace-each-occurrence-of-a-substring-independently-of-the-others

# Solution 1
import re

sentence = "it is a stupid book and a stupid hat and a stupid computer"

for match in re.finditer(r'\bstupid\b', sentence):
    print(sentence[:match.start()] + 'silly' + sentence[match.end():])

# Solution 2
def replaceEach(haystack, needle, replacement):
    pieces = haystack.split(needle)
    for i in range(len(pieces) - 1):
        yield needle.join(pieces[:i+1]) + replacement + needle.join(pieces[i+1:])