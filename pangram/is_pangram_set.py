def is_pangram_set(sentence):
    ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    alphabetSet = set(ascii_letters)
    for letter in sentence:
        if letter in alphabetSet:
            alphabetSet.remove(letter)
    if len(alphabetSet) == 0:
        return "This is a pangram!"
    else:
        return "Not a pangram."
    print(alphabetSet)

print(is_pangram_set("The quick brown fox jumps over he lazy dog"))
