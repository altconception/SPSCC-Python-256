num = input("Please type in a port number")

num = int(num)



while True:
    if num == 80 or num == 443 or num == 53:
            print("Proceed")
            break
    else:
          num = input("Please type in a port number")
          continue

    
    
