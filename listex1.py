firstlis = [2, 2, 2, 3]
secondlis = [2, 1, 3, 3]
total = []
for num1, num2 in zip(firstlis, secondlis):
    total.append (num1 *num2)
print(total)