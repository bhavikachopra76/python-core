# Q8. Create a program to count the number of vowels in a string.
s = input("Enter a string: ")
count = 0
for i in s.lower():
    if (i == 'a') | (i == 'e') | (i == 'i') | (i == 'o') | (i == 'u'):
        count = count + 1
print(f"Number of vowels are {count}")