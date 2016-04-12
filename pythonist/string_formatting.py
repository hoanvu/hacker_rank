# HackerRank - String Formatting
# https://www.hackerrank.com/contests/pythonist/challenges/python-string-formatting

number = int(raw_input(""))

for num in range(1, number + 1):
    width = len(bin(number)[2:]) + 1
    int_w = width - 1
    
    # Binary has '0b' at the beginning, remove them
    b = bin(num)[2:]
    # Octal has '0' at the beginning, remove it
    o = oct(num)[1:]
    # Hexadecimal has '0x' at the beginning, remove them
    h = hex(num)[2:].upper()
    
    # Using format() function to format the output
    # **locals() takes the values of variables 'width' and 'int_w'
    print "{0:>{int_w}}{1:>{width}s}{2:>{width}s}{3:>{width}s}".format(num, o, h, b, **locals())
