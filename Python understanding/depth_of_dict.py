# Write a code to find the depth of a dict.
# Depth of the dict - max depth of a dict
# depth - I a nested dict, going from one key to next nexted key till there is no more key will be described as depth of key.

def depth(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(depth(d[key], level+1) for key in d)
# Driver code
dic = {1: 'a', 11:{11:{11:{11:{}}}}, 2: {3: {4: {5:{},6:{}}}}}

print(depth(dic))
