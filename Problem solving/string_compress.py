# s = abcaaabbb e/o - abca3b3
# s=abcd e/o abcd
# s=aaabaaaaccaaaaba e/o - a3ba4c2a4ba

st=[]
#start=0, temp=s[0],1  ;
def compress_rec(s, start, temp):
    '''Recursive way to do the same thing.'''
    if start == len(s)-1:
        st.append(temp[0])
        st.append(str(temp[1]))
        print ''.join(st)
        return

    if s[start] == s[start+1]:
        temp = s[start], temp[1]+1

    else:
        st.append(temp[0])
        st.append(str(temp[1]))
        temp = s[start+1],1

    compress_rec(s, start+1, temp)

def compress(s):
    '''Iterative way'''
    i=0;count=1; temp=s[0],1
    while(i<=len(s)-1):
        if i==len(s)-1:
            st.append(temp[0])
            st.append(str(temp[1]))
            return (''.join(st))

        if s[i] == s[i+1]:
            count+=1
            temp=s[i],count

        else:
            st.append(temp[0])
            st.append(str(temp[1]))
            temp = s[i+1],1
            count =1
        i=i+1

s = 'aaaabaaaaccaaaaba'
compress_rec(s,0, (s[0],1))