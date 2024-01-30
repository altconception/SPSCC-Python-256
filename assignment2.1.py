num = input("Please type in a port number, either HTTP, HTTPS, or DNS: ")

num = int(num)

if num == 80:
    print("This is HTTP")
elif num == 443:
    print("This is HTTPS")
elif num == 53:
    print("This is DNS")
else:
    if num <= 1023:
        print("This is a well-known port")
    elif num > 1023 and num <= 49152:
        print("This is a registered port")
    else:
        print("This is a dynamic port")