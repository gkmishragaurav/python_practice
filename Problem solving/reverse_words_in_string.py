# Given an input string s, reverse the order of the words.
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.


s = " abc pqr    xyz "
s = s.split(" ")
print(s)
start = 0
end = len(s) - 1

while end > start:
    if not s[start]:
      start+=1
    elif not s[end]:
      end-=1
    else:
      s[start], s[end] = s[end], s[start]
      start += 1
      end -= 1

print(" ".join(item for item in s if item))
