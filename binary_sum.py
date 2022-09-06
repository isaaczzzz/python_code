import sys

sources = sys.argv[1:]

answer = 0

for i in sources:
    answer = answer + int(i, 2)

print(bin(answer)[2:])