def break_word(stuff) :
    """This function will break up words for us."""
    words = stuff.split()
    return words

def sort_word(words) :
    """sort the words."""
    return sorted(words)

def print_first_word(words) :
    """Print first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words) :
    """Print last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence) :
    """Takes in a full sentence and returns the sorted words."""
    words = break_word(sentence)
    return sorted(words)

def print_first_and_last(sentence) :
    """Print the first and last words of sentence."""
    words = sentence.split()
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence) :
    """Sort the words then print first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
