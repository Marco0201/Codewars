# When provided with a letter, return its position in the alphabet.

# Input: : "a"

# Ouput: : "Position of alphabet: 1"

def position(alphabet):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alp = list(alph)
    post = (new_alp.index(alphabet)) + 1
    return f"Position of alphabet: {post}"
