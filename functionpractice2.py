def octsplit():
    addr = input("Put an IP address: ")
    octs = addr.split(".")
    while len(octs) != 4:
        addr = input("Put an IP address: ")
        octs = addr.split(".") 
        continue
    else:
        return octs[0]


def ipChecker(oct1):
    try:
        oct1 = int(oct1)
        if oct1 <= 126:
            print("This is a class A")
        elif oct1 <= 191:
            print("This is a class B")
        elif oct1 <= 224:
            print("This is a class C")
        elif oct1 <= 254:
            print("This is a class D")
        else:
            print("This is not a valid IP")

    except ValueError:
        print("This is not a number")
    except KeyboardInterrupt:
        print("Bye!")
    except:
       print("Something went wrong")
    
ipChecker(octsplit())