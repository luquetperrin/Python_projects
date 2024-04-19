tuple = (2, 56, 34, 3, 5, -1)

for i in tuple:
    print(i)
else:
    print("Loop successfully completed and we are in else block now!!")


tuple1 = (2, 56, 34, 3, 5, -1)

for i in tuple1:
    if (i == 3):
        break
else:
    print("This block will not be completed")
print("Out of for/else")