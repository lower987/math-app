print()
print("This is just the start...")
print("The start of one of the best mathmatisian in the world...")
x = input("Will you be that one? ").lower()
if x == "yes":
    print("Great! Let's change the world.")
    print("The training starts now...")
else:
    print("Dont worry, you'll be here again.")
print()

import random
def easy():
    quest = 1
    c = 1
    while quest <= 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        print(f"{c}) What is {a} + {b}?")
        result = int(input("Your answer is: "))
        if result == (a+b):
            print("That's correct!")
            print()
            quest += 1
        else:
            print(f"That's incorrect, the real answer is {a+b}.")
            print("Let's do another one.")
            print()
        c += 1
    c -= 1
    print(f"Good job, you passed the first level in {c} attempts!")
        
easy()
