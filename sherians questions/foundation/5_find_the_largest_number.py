# Q5. Write a program to find the largest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b) & (a > c):
    print(f"\n{a} is greater than {b} and {c}")
elif (b > a) & (b > c):
    print(f"\n{b} is greater than {a} and {c}")
else:
    print(f"\n{c} is greater than {a} and {b}")