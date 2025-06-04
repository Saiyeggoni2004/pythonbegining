a=int(input("enter  a num"))
k=0
if a<1:
    print("1 is not a prime number")
    for i in range(2,a):
        a%i==0
        k+=1
        if k==2:
            print("num is prime a")
            
        else:
            print("num is not a prime a")
        
n=int(input("enter a number"))

k=0
for i in range (2,n):
    if n % i !=0:
        k+=1
if k==1:
    print(n, "is prime")
else:
    print(n,"is not prime")
s="hello\nworld"
print(s)

a=['hello world']
b="".join(a)
print(b)
   
string = "Hello, World!"

index = string.find("i")
print(index)
a = string.index("o")
print(a)
      
x=[[1,2,3],['a','b','c']]
for i in x:
    for j in i:
        print(j,end=" ")
    print()
y="sai.sagar"
for i in y:
    if i== ".":
        break
    print(i)
y="sai. sagar"
for i in y:
    if i== ".":
        break
    print(i,end="")
z="sai. sagar"
for i in z:
    if i== ".":
        continue
    print(i,end="")
    
for k in range(2,9):
    if k ==5:
        pass
    print(k)
printing sum of even numbers in btw 0 to 10
i=0
sum=0
while i<=10:
    if i%2==0:
        sum+=i
        i+=2
    print(sum)

    
reversing the string or number    
n=int(input("enter number"))
n_reverse=0
while n%10!=0:
    x=n%10
    n_reverse=n_reverse * 10 + x
    n=n//10
    print(n_reverse)
    
    
    

      

