# Q11. Write a program to find the sum of first N natural numbers.
n = int(input("Enter a number: "))
add = 0
for i in range(1, n+1):
    add = add + i
print(add)