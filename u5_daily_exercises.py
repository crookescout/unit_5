# Scout Crooke, 10/17/19, this program works on unit 5 daily exercises

import random

for x in range(21):
    print(x)


n = int(input("What is the upper value?"))
for y in range(1, n + 1):
    print(y)


print("Be careful, the upper value can not be smaller than the lower value!")
m = int(input("What is the lower value?"))
n = int(input("What is the upper value?"))
for y in range(m, n + 1):
    print(y)


a = int(input("What is the lower value?"))
b = int(input("What is the upper value?"))
for z in range(a, b - 1, -1):
    print(z)

print("Here are the numbers from 10 to 20:")
for x in range(10, 21):
    print(x)

print("Here are the even numbers from 2 to 40:")
for x in range(2, 41, 2):
    print(x)

n = int(input("What is the positive integer you want the multiplication table for?"))
for x in range(13):
    print(n, "*", x, "=", x * n)

for x in range(10):
    num = random.randint(1, 100)
    print(num)
