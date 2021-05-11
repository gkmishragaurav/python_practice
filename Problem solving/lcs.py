# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters 
# (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

def lcs(text1, text2):
    if not text1 or not text2:
        return 0
    if text1[0] == text2[0]:
        return 1+ lcs(text1[1:], text2[1:])

    return max(
        lcs(text1[1:], text2),
        lcs(text1, text2[1:])
    )


print(lcs("ylqpejqbal", "yrkzavgdmd"))
