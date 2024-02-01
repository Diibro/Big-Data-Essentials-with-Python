num1 = int(input("Enter num1: "))
num2  = int(input("Enter num2: "))

sumNum = num2 + num1
subNum = num2 - num1
multiNum = num2 * num1
divNum = num2 / num1
divNum2 = num2 // num1
rem = num2 % num1
power = num2 ** num1

print('Addition: ', sumNum)
print('Subtraction: ', subNum)
print('multiplication: ', multiNum)
print('division: ', divNum)
print('floor division: ', subNum)
print('rem: ', rem)
print('power: ', power)
print(id(power))