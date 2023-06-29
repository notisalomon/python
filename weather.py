import time

temp = int(input("How is the temperature today?: "))
time.sleep(0.4)
if temp >= 0 and temp <= 12:
    print("Seems to be cold outside. If you go out, wear a jacket!")
    time.sleep(2.4)
    print("I saw that Manor offers some really warm jackets for a discounted price.")
    time.sleep(2.2)
    offer = input("Are you interested?: ")
elif temp <= 13 or temp <= 30:
    print("Oh wow, seems to be nice out there. What are you doing here? Go out!")
    time.sleep(2.6)
    print("Galaxus has some great offers for rubber boats.")
    time.sleep(1.2)
    offer_galaxus = input("You want to take a look?: ")

time.sleep(0.5)

# if temp >= 0 and temp <= 12:
    # print("I saw that Manor offers some really warm jackets for a discounted price.")
    # time.sleep(2.8)
    # offer = input("Are you interested?: ")
# elif temp <= 13 or temp <= 30:
    # print("Galaxus has some really great offers for rubber boats.")
    # time.sleep(1.3)
    # offer_galaxus = input("You want to take a look?: ")
