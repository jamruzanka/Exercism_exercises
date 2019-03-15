"""An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
For example:
--9 is an Armstrong number, because 9 = 9^1 = 9
--153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153"""

def number_split(number):
    digits = [int(n) for n in str(number)]
    return digits

def is_armstrong(number):
    digits = number_split(number)
    sum = 0
    power = len(digits)
    for x in digits:
        y = x ** power
        sum += y
    return sum

print(is_armstrong(1234))
