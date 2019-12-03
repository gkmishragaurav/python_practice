dp=[]
def depth(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    for key in d:
        temp=depth(d[key], level + 1)
        if temp:
            dp.append(temp)
    return max(dp)
    # return max(depth(d[key], level+1) for key in d)
# Driver code
dic = {1: 'a', 11:{11:{11:{11:{}}}}, 2: {3: {4: {5:{},6:{}}}}}

print(depth(dic)), max(dp)
