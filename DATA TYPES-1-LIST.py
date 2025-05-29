# Empty list
empty_list = []

# List of integers
int_list = [1, 2, 3, 4]

# List of strings
str_list = ["apple", "banana", "cherry"]

# Mixed data types
mixed_list = [1, "hello", 3.14, True]

# Nested list (list of lists)
nested_list = [[1, 2], [3, 4]]

# List from a string (using list constructor)
char_list = list("hello")  
my_list = [10, 20, 30, 40, 50]

# Accessing elements
print(my_list[0])   
print(my_list[-1])  

# Slicing
print(my_list[1:4])  
print(my_list[:3])   
print(my_list[::2])  
#ADDING ELEMENTS
lst = [1, 2, 3]

lst.append(4)
lst.insert(1, 100)     
lst.extend([5, 6])     
#REMOVING ELEMENTS
lst.remove(100)        
lst.pop()           
lst.pop(1)      
del lst[0]             
lst.clear()         
#SEARCHING ELEMENTS
lst = [1, 2, 3, 4, 5]

print(lst.index(3)) 
print(4 in lst)        
print(lst.count(2))    
#SORTING AND REVERSING
numbers = [4, 2, 9, 1]
numbers.sort()         
numbers.sort(reverse=True)  
numbers.reverse()      
#Looping Through a List
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Using enumerate
for index, fruit in enumerate(fruits):
    print(index, fruit)
