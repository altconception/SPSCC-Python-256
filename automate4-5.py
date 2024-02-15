'''
Base fee - 40
Rooms
Bedroom - 10
Bathroom - 20
Living room - 15
# Living room also refers to alternate names: Family room, Great room, etc.)
Kitchen - 20
Dining room - 15
Mud room / laundry room - 10
Stairs / hallway - 10
'''
def calcCost():
    

    print("How many of each do you have?\n ")
    def howmany(a):
        b = input("How many " + a + "? ")
        while True:
            try:
                b = int(b)
                while b > -1:
                    break
                else:
                    b = input("How many "+ a + "? Please use a valid number. ")
                    continue
                break
            except:
                b = input("How many " + a + "? Please use a valid number. ")
                continue
        return b
    
    #bednum, bathnum, livingnum, kitchennum, diningnum, mudnum, stairsnum
    bed = howmany("beds")
    bath = howmany("baths")
    live = howmany("living rooms")
    kitchen = howmany("kitchens")
    dine = howmany("dining rooms")
    mud = howmany("mud rooms or laundry rooms")
    stair = howmany("stairs or hallways")
    
    bed = int(bed)
    bath = int(bath)
    live = int(live)
    kitchen = int(kitchen)
    dine = int(dine)
    mud = int(mud)
    stair = int(stair)
    #amenaties = [bed, bath, live, kitchen, dine, mud, stair]

    def cost(a, b):
        costDict = {"bed":10, "bath":20, "living":15, "kitchen":20, "dining":15, "mud":10, "stairs":10}
        #a is the key
        #b is the value to multiply by
        value = costDict[a]
        value *= b
        return value
    
    z = cost("bed", bed)
    y = cost("bath", bath)
    x = cost("living", live)
    w = cost("kitchen", kitchen)
    v = cost("dining", dine)
    u = cost("mud", mud)
    t = cost("stairs", stair)
    

    print("You must fork over $" + str(int(t + u + v + w + x + y + z) + 40) + "!!!")

calcCost()







