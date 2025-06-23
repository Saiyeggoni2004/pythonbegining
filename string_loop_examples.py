# Problem 1: Demonstrate newline character in a string
s = "hello\nworld"
print(s)

# Problem 2: Join a list of strings into a single string
a = ['hello world']
b = "".join(a)
print(b)

# Problem 3: Use of find() and index() string methods
string = "Hello, World!"
index = string.find("i")  # find() returns -1 if not found
print(index)
a = string.index("o")     # index() raises an error if not found
print(a)

# Problem 4: Nested list iteration with formatted output
x = [[1, 2, 3], ['a', 'b', 'c']]
for i in x:
    for j in i:
        print(j, end=" ")
    print()

# Problem 5: Break loop on encountering a period character
y = "sai.sagar"
for i in y:
    if i == ".":
        break
    print(i)

# Problem 6: Print characters until a period without newline
y = "sai. sagar"
for i in y:
    if i == ".":
        break
    print(i, end="")

# Problem 7: Skip period and print remaining characters
z = "sai. sagar"
for i in z:
    if i == ".":
        continue
    print(i, end="")

# Problem 8: Demonstrate pass statement in a loop
for k in range(2, 9):
    if k == 5:
        pass  # Placeholder; does nothing
    print(k)
