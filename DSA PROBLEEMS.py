#Find the Largest Element in a List
a=[2,3,4,5,6,75,6,3,2,100]
a.sort()
b=len(a)
print(a[b-1])
#Count How Many Characters in b Exist in a (Once per Character)
a="aabbccdd"
b="abcd"
c=0
for i in b:
    for j in a:
        
        if i==j:
            c+=1
            break
print(c)
 #Count Words in a List    
s=["sai sagar","sai sagar yeggoni"]
a=" ".join(s)s.split()
c=0
for i in range(len(a)):
    print(i)
    c+=1
print(c)
#Count Number of Words in Each String in a List

s=["sai sagar","sandy dad1", "sai tej kumar"]

for i in range (len(s)):
    a=s[i]
    
    b+=1
    for j in range(len(a)):
        if a[j]==" ":
            b+=1
            
    print(b)
