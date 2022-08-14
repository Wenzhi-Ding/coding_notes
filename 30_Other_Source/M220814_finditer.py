# https://stackoverflow.com/questions/73349913/how-can-i-replace-each-occurrence-of-a-substring-independently-of-the-others

import re

sentence = "it is a stupid book and a stupid hat and a stupid computer"

for match in re.finditer(r'\bstupid\b', sentence):
    print(sentence[:match.start()] + 'silly' + sentence[match.end():])