import random
list1 = [1,3,2,4,3,5,3]
cond = True

while cond:
     choice = random.choice(list1)
     userChoice = int(input("choose a number: "))
     if userChoice == choice:
          print("You passed !!!!")
          cond = False
     else:
          print("The number was: ", choice)
          print("You got it wrong try again")

print(choice)