"""this is the questions/solutions to chapter 12 arcade - advanced looping"""

# Problem 1: write code that will print ten asterisks (*) in a row:
for i in range(10):
    print("*", end=" ")
print()

# problem 2: Write code that will print the following:
# * * * * * * * * * *
# * * * * *
# * * * * * * * * * * * * * * * * * * * *
asterisk_count = [10, 5, 20]
for item in asterisk_count:
    for i in range(item):
        print("*", end=" ")
    print()
print()

# problem 3: Use two “for” loops, one of them nested inside the other, to print a 10x10 rectangle:
for row in range(10):
    for column in range(10):
        print("*", end=" ")
    print()
print()

# problem 4: Use two “for” loops, one of them nested, to print a 5x10 rectangle:
for row in range(10):
    for column in range(5):
        print("*", end=" ")
    print()
print()

# problem 5: Use two for loops, one of them nested, to print a 20x5 rectangle:
for row in range(5):
    for column in range(20):
        print("*", end=" ")
    print()
print()

# problem 6: Write code that will print the following:
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
for row in range(10):
    for i in range(0, 10):
        print(i, end=" ")
    print()
print()

# problem 7: Adjust the prior program to print:
# 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2 2 2 2
# 3 3 3 3 3 3 3 3 3 3
# 4 4 4 4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5 5
# 6 6 6 6 6 6 6 6 6 6
# 7 7 7 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9 9
for i in range(0, 10):
    for j in range(10):
        print(i, end=" ")
    print()
print()

# problem 8: Write code that will print the following:

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7 8 9
for i in range(0, 11):
    for j in range(0, i):
        print(j, end=" ")
    print()
print()

# problem 9: Write code that will print the following:
#
# 0 1 2 3 4 5 6 7 8 9
#   0 1 2 3 4 5 6 7 8
#     0 1 2 3 4 5 6 7
#       0 1 2 3 4 5 6
#         0 1 2 3 4 5
#           0 1 2 3 4
#             0 1 2 3
#               0 1 2
#                 0 1
#                   0
for row in range(9, -1, -1):
    for space in range((10 - row) * 2):
        print(end=" ")
    for column in range(row + 1):
        print(column, end=" ")
    print()

# problem 10: Write code that will print the following (Getting the alignment is hard, at least get the numbers):

# 1  2  3  4  5  6  7  8  9
# 2  4  6  8 10 12 14 16 18
# 3  6  9 12 15 18 21 24 27
# 4  8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81
for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:
            print(end=" ")
        print(i * j, end=" ")
    print()
print()
