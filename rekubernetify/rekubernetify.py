import re
import random

def make_pattern(s4g):
    first_letter = s4g[0]
    middle = s4g[1:-1]
    end_letter = s4g[-1]
    pattern = r"^" + first_letter + r"[a-z]{" + middle + r"}" + end_letter + "$"
    return pattern


def compile_reg(s4g):
    return re.compile(make_pattern(s4g), re.IGNORECASE)


def all_possible_words(s4g):
    matches = []
    reg = compile_reg(s4g)
    with open("words.txt", "r") as words:
        for line in words:
            if reg.match(line):
                matches.append(reg.match(line)[0])
    
    if len(matches) == 0:
        return s4g
    return matches


def unkubernetify(s4g):
    if len(s4g) < 3:
        return s4g
    #if re.match(r"\w", s4g):
        #return s4g
    #if re.match(r"[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/]", s4g):
        #return s4g
    words = all_possible_words(s4g)
    if isinstance(words, list):
        return random.choice(words)
    return s4g


def convert_sentence(long_string):
    words = long_string.split()
    new_words = []
    for word in words:
        new_words.append(unkubernetify(word))
    return " ".join(new_words)


print(convert_sentence(input("Enter Text:")))

