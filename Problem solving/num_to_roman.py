# Converting Decimal Number lying between 1 to 3999 to Roman Numerals

# SYMBOL       VALUE
# I             1
# IV            4
# V             5
# IX            9
# X             10
# XL            40
# L             50
# XC            90
# C             100
# CD            400
# D             500
# CM            900
# M             1000
# ---------------------------------------------------------
def make_string(num, ch, n):
    # This will make string for number n and give its char value as ch
    str=''
    d = num / n
    while(d):
        str = str + ch
        d = d - 1
    return str

def roman(num):
    str=''
    if num/1000>= 1:
        str = str + make_string(num, 'M', 1000)
        num = num % 1000

    if num/900>=1:
        str = str + 'CM'
        num = num % 900

    if num/500>=1:
        str = str + make_string(num, 'D', 500)
        num = num % 500

    if num/400>=1:
        str = str + 'CD'
        num = num % 400

    if num/100>= 1:
        str = str + make_string(num, 'C', 100)
        num=num%100

    if num/90 >= 1:
        str=str+'XC'
        num = num % 90

    if num/50 >= 1:
        str = str + make_string(num, 'L', 50)
        num = num % 50

    if num/40 >= 1:
        str=str+'XL'
        num = num % 40

    if num/10>=1:
        str = str+make_string(num, 'X', 10)
        num=num%10

    if num == 9:
        str = str+'IX'
        num=0

    if num/5 >= 1:
        str=str+'V'
        num=num%5

    if num == 4:
        str = str+'IV'
        num=0

    while(num):
        str=str+'I'
        num=num-1

    print str

num = 14
roman(num)
# Ans - MMMDXLIX
