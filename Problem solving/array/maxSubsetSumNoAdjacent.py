# Maximum sum such that no two elements are adjacent
#
# [75, 105, 120, 75, 90, 135] -- 330 [75+120+135]

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    inclusive=array[0]
    exclusive=0
    i=1
    while i<len(array):
        temp = inclusive
        inclusive = exclusive + array[i]
        exclusive = max(temp, exclusive)
        i=i+1

    return max(inclusive, exclusive)

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 35]))
