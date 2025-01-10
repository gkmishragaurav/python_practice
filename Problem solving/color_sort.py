# Given an array, colors, which contains a combination of 0,1,2
# Sort the array in place so that the elements of the same color are adjacent, 
# with the colors in the order of red, white, and blue. 
# To improve your problem-solving skills, do not utilize the built-in sort function.


s = [0,0,1,0,2,1,0,1,2,0,1,0]

def sort_colors(colors):
    start, mid, end = 0, 0, len(colors) - 1
    while mid <= end:
        if colors[mid] == 0:
            colors[mid], colors[start] = colors[start], colors[mid]
            mid = mid + 1
            start = start + 1

        elif colors[mid] == 1:
            mid = mid + 1

        else:
            colors[end], colors[mid] = colors[mid], colors[end]
            end = end - 1
    # Replace this placeholder return statement with your code
    return colors

print(sort_colors(s))
