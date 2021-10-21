import sys
import random
import string
allowed = ["!", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]


def c_password():
    points = 0
    n = 0
    u = 0
    l = 0
    c = 0
    print("your password is valid!")
    p_count = len(password)
    for x in range(p_count):
        up_check = password[x].isupper()  # looks for uppercase letters
        n_check = password[x].isdigit()  # looks for number characters
        l_check = password[x].islower()  # looks for lower case letters
        c_check = password[x] in allowed
        if up_check:
            u += 1
        if n_check:
            n += 1
        if l_check:
            l += 1
        if c_check:
            c += 1
    if u >= 1:
        points += 5
    if n >= 1:
        points += 5
    if l >= 1:
        points += 5
    if c >= 1:
        points += 5
    if c and l and n and u >= 1:
        points += 5
    if c and n == 0:
        points -= 5
    if c and l and u == 0:
        points -= 5
    if n and l and u == 0:
        points -= 5
    return points


def g_password(allowed_chars, length ):
    print("You have chosen to generate a password :3")
    print("Your password is being generated ...")

    e = []
    for x in range(length):
         e.append("".join(random.choice(allowed_chars) ))
    return e
while True:

    print("\nA: Check Password \n\nB: Generate Password\n\nQ: quit\n")
    choice = input("Please choose A, B OR Q from the options provided").lower()

    if choice == "a":
            print("You have chosen to check your password :3")
            password = input("Please enter your password to be checked")
            if 8 <= len(password) <= 24:
                points = c_password()
                if points <= 0:
                    print("your password is weak")
                if points >= 20:
                    print("your password is strong")
                else:
                    print("your password is medium strength")

            else:
                print("Invalid password")
    if choice == "b":
        chars = string.ascii_letters + string.punctuation
        length = random.randint(8, 12)
        password = g_password(chars, length)
        print("Generated password is: ", password)

    if choice == "q":
        sys.exit("You have quit the program!")


