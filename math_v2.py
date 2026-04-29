import random
print()
print("-------------------------------------------")
print("Let's start with the math training session.")
print("You'll find different levels of difficulty.")
print("With 3 correct answers you pass each level.")
print("-------------------------------------------")
print()

def sum1():
    print("This is the sum level one.")
    quest = 1
    c = 1
    while quest <= 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        print(f"{c}) What is {a} + {b}?")
        result = int(input("Your answer is: "))
        if result == (a + b):
            print("That's correct!")
            print()
            quest += 1
        else:
            print(f"That's incorrect, the real answer is {a + b}")
            if result == (a + b - 1) or result == (a + b + 1):
                print("You were so close!!")
            print("Let's try again.")
            print()
        c += 1
    print(f"Good job, you passed this level in {c - 1} attempts!")
    print()

def sum2():
    print("This is the sum level two.")
    quest = 1
    c = 1
    while quest <= 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"{c}) What is {a} + {b}?")
        result = int(input("Your answer is: "))
        if result == (a + b):
            print("That's correct!")
            print()
            quest += 1
        else:
            print(f"That's incorrect, the answer is {a + b}")
            if result == (a + b - 1) or result == (a + b + 1):
                print("You were so close!!")
            print("Let's try again.")
            print()
        c += 1
    print(f"Good job, you passed this level in {c - 1} attempts!")
    print()

def multiply1():
    print("This is the multiply level one.")
    quest = 1
    c = 1
    while quest <= 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        print(f"{c}) What is {a} * {b}?")
        result = int(input("Your answer is: "))
        if result == (a * b):
            print("That's correct!")
            print()
            quest += 1
        else:
            print(f"That's incorrect, the answer is {a * b}")
            if result == (a * b - 1) or result == (a * b + 1):
                print("You were so close!!")
            print("Let's try again.")
            print()
        c += 1
    print(f"Good job, you passed this level in {c - 1} attempts!")
    print()

def multiply2():
    print("This is the multiply level two.")
    quest = 1
    c = 1
    while quest <= 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"{c}) What is {a} * {b}?")
        result = int(input("Your answer is: "))
        if result == (a * b):
            print("That's correct!")
            print()
            quest += 1
        else:
            print(f"That's incorrect, the answer is {a * b}")
            if result == (a * b - 1) or result == (a * b + 1):
                print("You were so close!!")
            print("Let's try again.")
            print()
        c += 1
    print(f"Good job, you passed this level in {c - 1} attempts!")
    print()

def division():
    print("This is the division level.")
    print("The numbers must be written with 2 decimals.")
    quest = 1
    c = 1
    while quest <= 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        print(f"{c}) What is {a} / {b}?")
        result = float(input("Your answer is: "))
        if result == float(f"{(a / b):.2f}"):
            print("That's correct!")
            print()
            quest += 1
        else:
            print(f"That's incorrect, the answer is {(a / b):.2f}")
            if result == (float(f"{(a / b):.2f}") - 0.01) or result == (float(f"{(a / b):.2f}") + 0.01):
                print("You were so close!!")
            print("Let's try again.")
            print()
        c += 1
    print(f"Good job, you passed this level in {c - 1} attempts!")
    print()

sum1()
sum2()
multiply1()
multiply2()
division()