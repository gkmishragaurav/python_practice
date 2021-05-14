# Write a function that takes in a "special" array and returns its product sum.
# A "special" array is a non-empty array that contains either integers or other
# "special" arrays. The product sum of a "special" array is the sum of its elements,
# where "special" arrays inside it are summed themselves and then multiplied by their level of depth.
# The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1 ;
# the depth of the inner array in [[]] is 2 ; the depth of the innermost array in [[[]]] is 3.
# Therefore, the product sum of [x, y] is x + y; the product sum of
# [x, [y, z]] is x + 2 * (y + z); the product sum of [x, [y, [z]]] is x + 2 * (y + 3z).
# [5, 2, [7, -1], 3, [6, [-13, 8], 4]] --- ans 12
def productSum(a, i, curr, key):
    if i == len(a):
        return curr

    if isinstance(a[i], list):
        temp = productSum(a[i], 0, 0, key+1)
        curr = curr+temp*(key+1)
    else:
        curr = curr+a[i]
    return productSum(a, i+1, curr, key)


a= [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(a, 0, 0, 1))
