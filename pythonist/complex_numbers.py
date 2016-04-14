# Hacker Rank - Math operations on Complex Numbers
# https://www.hackerrank.com/contests/pythonist/challenges/class-1-dealing-with-complex-numbers
import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, number):
        real = self.real + number.real
        imaginary = self.imaginary + number.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, number):
        real = self.real - number.real
        imaginary = self.imaginary - number.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, number):
        real = self.real * number.real - self.imaginary * number.imaginary
        imaginary = self.real * number.imaginary + self.imaginary * number.real
        return ComplexNumber(real, imaginary)

    def __div__(self, number):
        denominator = number.real ** 2 + number.imaginary ** 2
        real = (self.real * number.real + number.imaginary) / denominator
        imaginary = (self.real * (-number.imaginary) + self.imaginary * number.real)
        imaginary /= denominator
        return ComplexNumber(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return ComplexNumber(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary > 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

cn1 = ComplexNumber(42, -42)
cn2 = ComplexNumber(84, -84)

print cn1 + cn2
print cn1 - cn2
print cn1 * cn2
print cn1 / cn2
print cn1.mod()
print cn2.mod()
