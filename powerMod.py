def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


def powMod(a,b,m):
    x = b%m
    y = (a%m)%m
    print x
    print y
    print x*y

    return ((b%m)*((a%m)%m))%m




print (8**4)%7
print pow_mod(2,3,5)
print pow_mod(pow_mod(2,3,7),4,7)

# print pow_mod(2,5,3)
# print powMod(2,5,3)
# print pow_mod(26,13,54)
# print powMod(26,13,54)