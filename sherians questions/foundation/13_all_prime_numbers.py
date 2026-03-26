# Q13. Write a program to print all prime numbers between 1 and 100.
import math
def check_prime(num): #2
    flag = True
    for x in range(2,(math.isqrt(num))+1):
        if num%x == 0:
            flag = False
            break
    if flag:
        return True
    else:
        return False

for i in range(2, 101):
    if check_prime(i):
        print(i , end = " ")