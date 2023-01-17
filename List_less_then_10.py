## Lists comprehensions with loops
print("_____________________________________________")
print("Welcome! We are gonna have a look at some lists")
print("This is done with list comprehension")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
# 1
c =[i for i in a if i < 10]
print(c)

print("_____________________________________________")
print("And, this is a for-loop, that does the same thing")
# 2
for i in a:
    if i < 10:
        b.append(i)
print(b)

print("____________________________________________")
print("Here comes a interactive program using lists")
# 3 - program

num = input("Provide any positive integer:")
c2 =[i for i in a if i < int(num)]

print(c2)

print("That was all for this time, Bye!!")
print("____________________________________________")