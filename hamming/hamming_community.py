def distance(seq1, seq2):
    return sum(1 if a != b else 0 for a, b in zip(seq1, seq2))

str_a = 'GAGCCTACTAACGGGATKDK'
str_b = 'CATCGTAATGACGGCCTLMK'

print(distance(str_a, str_b))
