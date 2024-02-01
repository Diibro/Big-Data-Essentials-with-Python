num1 = 4
name1 = "Dushime Brother"
cond = True
complexnum = 2+4j
char = 'e'
# print("num1 is: ", type(num1))
# print("name1 is: ", type(name1))
# print("cond is: ", type(cond))
# print("The complexnum is: ", type(complexnum))
# print("char is: ", type(char))
# print(len(name1))

string = input("Enter elements separated by space")
lst  = string.split()
lst1 = lst[0][:4]
lst2 = lst[0][::-1]
print("List of entered elements are :", lst2, " and the array obtained is: ", len(lst))