# Q10. Check if a number is a palindrome.
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp != 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp//10

if num == rev:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")