# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    words = list(s)
    non = []
    for i in words:
        if i != '!':
            non.append(i)
        else:
            pass
    return ''.join(non)
