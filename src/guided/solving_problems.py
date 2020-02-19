# write a function power() that given value a and exponent b will compute a^b
# It would be silly to have the function say return a^b, we won't learn anything...

def power(value, exponent):
    # What is 2^3
    # 2*2*2

    # problem 1
    # if exponent == 1:
    #     return value
    #problem 2
    # if exponent == 2:
    #     return prob1Value * value
    #problem 3
    # if exponent == 3:
    #     return prob2Value * value

    # What about negative number
        # X ^-n == 1 / x ^ n
    # What about fractions??
    # what about zero
    if not exponent.is_interger():
        print('Sorry')
        return 

    if exponent < 0:
        exponent += -1
        value = 1 /value
    # base case
    if exponent == 0:
        return 1

    return value * power(value, exponent -1)
print(power(4,3))
