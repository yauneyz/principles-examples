import random

name = input("What is your name")

# Determine if
r = random.randint(0, 1)


def message(choice):
    for i in range(10):
        if choice == 0:
            start = "Hello"
        else:
            start = "Goodbye"

    answers = [start, name]

    print(answers[0] + " " + answers[1])


message(r)
