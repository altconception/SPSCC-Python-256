grade = input("Input your grade: ")

grade = int(grade)

if grade >= 92:
    if grade >= 95:
        print("You got an A")
    else:
        print("You got an A-")
elif grade >= 83:
    if grade >= 88:
        print("You got a B+")
    elif grade >= 85:
        print("You got a B")
    else:
        print("You got a B-")   
elif grade >= 74:
    if grade >= 79:
        print("You got a C+")
    elif grade >= 76:
        print("You got a C")
    else:
        print("You got a C-")
elif grade >= 65:
    if grade >= 71:
        print("You got a D+")
    elif grade >= 68:
        print("You got a D")
    else:
        print("You got a D-")
else:
    print("You failed :(")