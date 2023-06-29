temp = int(input("How is the temperature today?: "))

if temp >= 0 and temp <= 12:
    print("Seems to be cold outside. If you go out, wear a jacket!")
elif temp <= 13 and temp <= 30:
    print("Oh wow, seems to be nice out there. What are you doing here? Go out!")
