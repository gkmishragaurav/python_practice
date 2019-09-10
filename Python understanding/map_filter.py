num=[1,2,3,4,5,6,7,8,9,10]
chars = 'yEFfERGg,UKweuTHgheUKLrjOer'
grades = (81, 89, 94, 78, 51, 66, 99,74)

def find_odd(num):
    if num%2==1: return True
    return False

def is_upper(ch):
    if ch.lower() != ch: return True
    return False

def grade_mapping(g):
    if 100>=g>=90:
        return 'A'
    elif 90>g>=80:
        return 'B'
    elif 80>g>=70:
        return 'C'
    elif 70>g>=60:
        return 'D'
    return 'F'


def square(n):
    return n**2

# finding all odd numbers
odds = list(filter(find_odd, num))
print odds

# finding all upper case charecters.
upper = list(filter(is_upper, chars))
print upper

# retuen all squares
squares = list(map(square, num))
print squares

# mapp grades
grading = list(map(grade_mapping, grades))
print grading