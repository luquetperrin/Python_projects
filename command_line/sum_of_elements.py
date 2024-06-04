# Sum of all elements from the command line
import sys

sum = 0
for i in range(1, len(sys.argv)):
               sum += int(sys.argv[i])
print("Result=", sum)
