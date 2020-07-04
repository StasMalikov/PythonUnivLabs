s = [2,11,8,11,2,3,2,2,6,7,2,3,5,10]
#s= [1,2,3,4,5,6,7,8,9,10,11]
print(s)

index1=0
i=0
while i<len(s):
    if(min(s)==s[i]):
            index1=i
    i+=1
index2=s.index(max(s))

i=0
if(index2>index1):
     while i<(-index1+index2)/2-1:
        s[index2-i-1],s[index1+i+1]=s[index1+i+1], s[index2-i-1]
        i+=1
        print(s)
else:
    while i<(index1-index2)/2-1:
        s[index2+i+1],s[index1-i-1]=s[index1-i-1], s[index2+i+1]
        i+=1
        print(s)