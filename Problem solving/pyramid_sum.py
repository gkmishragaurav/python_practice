# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ......
#
# Find the sum of all the integers in the row number N.
# For example:
# The row #3: 4 + 5 + 6 = 15
# The row #5: 11 + 12 + 13 + 14 + 15 = 65

# n is number of the line
n=400
j=1
pyramid=[]
for i in range(1,n+1):
    temp=[]
    while(len(temp)<i):
        temp.append(j)

        j=j+1

    pyramid.append(temp)

print pyramid[n-1]
sum=0
# sum for nth coloum
for x in pyramid[n-1]:
    sum=sum+x

print sum
