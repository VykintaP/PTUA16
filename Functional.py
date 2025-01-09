
starts_with = lambda s, char: s[0] == char
print(starts_with("hello","h"))

def starts (letters, first_letter):
    return letters[0] == first_letter
print(starts("hello","h"))

finishes_with = lambda word, character: word[-1] == character
print(finishes_with("hello","o"))