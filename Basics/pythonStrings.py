names = input("enter your full names: ")
lst =list( names.split())
newName = "".join(reversed(lst[0]))
lst2 = list(lst[0])
lst2[0] = 'S'
finalName = "".join(lst2)
print(lst)
print(finalName)