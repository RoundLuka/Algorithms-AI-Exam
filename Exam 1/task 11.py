"""11) დაწერეთ კოდი რომელიც გადაიყვანს რიცხვებს ათობითი სისტემიდან ორობითში და პირიქით"""

def dec_to_bin(number):
    rem = ""
    while number != 0:
        rem += str(number % 2)
        number = number // 2
    return (rem[::-1])

print(dec_to_bin(234))
print(dec_to_bin(46))

def bin_to_dec(bin_number):
    strng = (str(bin_number))[::-1]
    result = 0
    for i in range(len(strng)):
        digit = int(strng[i])
        result += digit * (2 ** i)
    return result

print(bin_to_dec(100101))
print(bin_to_dec(1101))
print(bin_to_dec(10010111))