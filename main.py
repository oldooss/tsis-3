#1
#
# def converterForGram(ounces):
#     gramm = float(28.3495231)
#     total = ounces * gramm
#     return total
#
# ounces = int(input("total number of ounces: "))
# print(converterForGram(ounces))

#2

# F = int(input("Fahrenheit: "))
# C = ((5/9) * (F - 32))
#
# print(C)

#3

# def solve(numheads, numlegs):
#     x = (numlegs - numheads * 2) / 2
#     return x
#
# a = int(input("heads: "))
# b = int(input("legs: "))
# z = solve(a, b)
# rabbit_head = z
# chicken_head = a - z
#
# print(rabbit_head, chicken_head)

#4

# from math import sqrt
#
# def filter_prime(num):
#     for i in range(2, int(sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# numbersForCheck = [2, 3, 4, 5, 11, 15, 20]
#
# for i in numbersForCheck:
#     if filter_prime(i):
#         print(i)

#5

# from itertools import permutations
#
# def fpermutation(text):
#     permList = permutations(text)
#     for perm in list(permList):
#         print(''.join(perm))
#
#
# text = input()
# fpermutation(text)

#6

# def reverseStr(str):
#     s = str.split()[::-1]
#     l = []
#     for i in s:
#         l.append(i)
#     return " ".join(l)
#
# text = "we are ready"
# print(reverseStr(text))

#7

# def has_33(x):
#     current = None
#     for item in x:
#         if current == item == 3:
#             return True
#         current = item
#     return False
#
# list_3 = [1, 3, 3, 5]
# print(has_33(list_3))

#8

# def spy_game(num):
#     count = 0
#     for i in num:
#         if i == 0:
#             count += 1
#         else:
#             pass
#         if i == 7:
#             count += 1
#             break
#     return count == 3
#
# print(spy_game([1,7,4,0,0,0,5]))
# #doesnt work properly

#9

# def vol(rad):
#     pi = 22/7
#     volume = (4/3) * (pi * rad ** 3)
#     return volume
#
# radian = float(input("Radius of sphere: "))
# print(vol(radian))

#10

# def unique_list(li):
#     x = []
#     for i in li:
#         if i not in x:
#             x.append(i)
#     return x
#
# print(unique_list([1,2,3,3,3,3,4,5]))

#11

# def check_pol(x, y):
#     if x == y:
#         print("String is palindrome.")
#     else:
#         print("String is not palindrome.")
#
# text = input("Enter a string: ")
# rev = text[::-1]
#
# check_pol(text, rev)

#12

# def histogram(x):
#     for i in range(len(x)):
#         print(x[i] * '*')
#
# listOfNum = [4,9,7]
#
# histogram(listOfNum)

#13
import random

print("Hello! What is your name? ")
name = input("")

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
number = int(input(""))
numHaveToFind = random.randint(1, 20)
print(numHaveToFind)
score = 0

isTrue = True

while isTrue:
    if number > numHaveToFind:
        print("Your guess is too high")
        score += 1
        number = int(input(""))
    elif number < numHaveToFind:
        print("Your guess is too low")
        score += 1
        number = int(input(""))
    elif number == numHaveToFind:
        print(f"Good job, {name}! You guessed my number in {score} guesses!")
        isTrue = False