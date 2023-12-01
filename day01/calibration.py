# load the input
with open('day01/input.txt') as f:
    text = f.readlines()


digit_set = set('0123456789')
digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
word_to_digit = {word: (i+1) for i, word in enumerate(digit_words)}

# make a trie
trie = {}
for word in digit_words:
    curr = trie
    for c in word:
        if c not in curr:
            curr[c] = {}
        curr = curr[c]
    curr['end'] = True
    
def word_digit(word):
    curr = trie
    for i, c in enumerate(word):
        if c not in curr:
            return None
        curr = curr[c]
        if 'end' in curr:
            return word_to_digit[word[:i+1]], i+1

def is_char_digit(char):
    return char in digit_set

def get_calibration(line):
    first_digit = None
    curr_digit = None
    i = 0
    while i < len(line):
        c = line[i]
        if is_char_digit(c):
            curr_digit = int(c)
            i+=1
        else:
            wi = word_digit(line[i:])
            if wi is not None:
                curr_digit, j = wi
                i+=1 # skip the word
            else:
                i+=1
        if first_digit is None and curr_digit is not None:
            first_digit = curr_digit
        
    return first_digit*10 + curr_digit


s = 0
for line in text:
    line = line.strip()
    s+= get_calibration(line)
print(s)
    
    

