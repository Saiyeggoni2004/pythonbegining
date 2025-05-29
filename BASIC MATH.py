#Convert Integer to Complex Number

a=8
print(complex(a))

print(complex(True))
#Convert Boolean to Complex Number
x=-4
print(bool(x))
x='0'
print(bool(x))
x=''
print(bool(x))
#Check for Leap Year (Simple Logic)
def is_leap(year):
    if year%4==0 :
        return True
    else:
        return False
        

year = 1990
print(is_leap(year))
#Swap Two Variables Without Temporary Variable
a=5
b=6
a=a+b
b=a-b
a=a-b

print(a)
print(b)
#using xor(^) swaping
a=9
b=7
a=a^b
b=a^b
a=a^b
print(a,b)
