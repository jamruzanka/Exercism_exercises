def distance(strand_a, strand_b):
    str_a = list(strand_a)
    str_b = list(strand_b)
    if len(str_a) == len(str_b):
        counter = 0
        for i in range(len(str_a)):
            if str_a[i] != str_b[i]:
                counter += 1
        return counter
    else:
        return("Strings not equal! Can't compare.")

str_a = 'GAGCCTACTAACGGGATKDKI'
str_b = 'CATCGTAATGACGGCCTLMO'

print(distance(str_a, str_b))
