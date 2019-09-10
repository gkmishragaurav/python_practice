# Find largest substring of contiguous, repeating character in a string, print the character and length of substring
# xyzzzzcba z,4
# xyzzzzcbbbababababa z,4
#

def largest_substring(a):
    i = 0
    count = 1
    max = 0
    save_char = ''
    while (i < len(a) - 1):
        if a[i] == a[i + 1]:
            count = count + 1
            if max < count:
                max = count
                save_char = a[i]
        else:
            count = 1
        i = i + 1

    return max, save_char


a = 'xyzzzzzcbaaa'
print largest_substring(a)