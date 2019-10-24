# Scout Crooke, 10/17/19, this program works on unit 5 daily exercises

import random

# for x in range(21):
#     print(x)
#
#
# n = int(input("What is the upper value?"))
# for y in range(1, n + 1):
#     print(y)
#
#
# print("Be careful, the upper value can not be smaller than the lower value!")
# m = int(input("What is the lower value?"))
# n = int(input("What is the upper value?"))
# for y in range(m, n + 1):
#     print(y)
#
#
# a = int(input("What is the lower value?"))
# b = int(input("What is the upper value?"))
# for z in range(a, b - 1, -1):
#     print(z)
#
# print("Here are the numbers from 10 to 20:")
# for x in range(10, 21):
#     print(x)
#
# print("Here are the even numbers from 2 to 40:")
# for x in range(2, 41, 2):
#     print(x)
#
# n = int(input("What is the positive integer you want the multiplication table for?"))
# for x in range(13):
#     print(n, "*", x, "=", x * n)
#
# even_sum = 0
# odd_sum = 0
# for x in range(10):
#     num = random.randint(1, 100)
#     if (num % 2) == 0:
#         even_sum = even_sum + num
#     else:
#         odd_sum = odd_sum + num
#
# print(even_sum)
# print(odd_sum)
#
# num_sum = 0
# for x in range(1000):
#     if (x % 3) == 0 or (x % 5) == 0:
#         num_sum = num_sum + x
#
# print(num_sum)

# x = 0
# num = int(input("Give me a number please"))
# while x < num + 1:
#     print("* " * x)
#     x = x + 1

# total = 0
# times = 0
# product = 1
# while True:
#     num = input("What number do you want to use?")
#     if num == "q":
#         break
#     print(num, "Press q to quit.")
#     num = int(num)
#     times += 1
#     total = total + num
#     product = product * num
# print("The average of your numbers was", total/times)
# print("The product of your numbers was", product)

# steps = 0
# num = int(input("What number do you want to use?"))
# while num != 1:
#     print(num)
#     if num % 2 ==0:
#         num = num / 2
#     else:
#         num = (num * 3) + 1
#     steps += 1
# print(num)
# print("It took you", steps, "steps")

# Project Euler Problem 14
for num in range(2, 999999):
    steps = 0
    biggest_num = 0
    num = int(input("What number do you want to use?"))
    while num != 1:
        print(num)
        if num % 2 ==0:
            num = num / 2
        else:
            num = (num * 3) + 1
        steps += 1
    if num > biggest_num:
        biggest_num = num
    print(num)
