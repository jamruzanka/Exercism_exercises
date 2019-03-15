def is_pangram(sentence):
    ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    sentence_letters = []
    for char in sentence:
        for letter in ascii_letters:
            if char == letter and char not in sentence_letters:
                sentence_letters.append(char)
    if len(sentence_letters) == 26:
        return True
    else:
        return False

print(is_pangram("The quick brown fox jumps over the lazy dog"))
