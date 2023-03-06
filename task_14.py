'''
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
'''
#https://pynative.com/python-basic-exercise-for-beginners/


def exponent(base,exp):
    r = 1
    for x in range (exp):
        r *= base
    return r


b = int(input("enter base:\n"))
e = int(input("enter exponent:\n"))
print(b, "raises to the power of", e, "is: ", exponent(b,e))