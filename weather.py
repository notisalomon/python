import time
import webbrowser
import sys

manor_url = 'www.manor.ch'
galaxus_url = 'www.galaxus.ch'

manor = {
        "question": "Are you interested? [Yes] or [No]: ",
        "Yes": ["Yes", "yes"],
        "No": ["No", "no"]
        }
galaxus = {
        "question": "You want to take a look? [Yes] or [No]: ",
        "Yes": ["Yes", "yes"],
        "No": ["No", "no"]
        }

temp = int(input("How is the temperature today?: "))
time.sleep(0.4)
if temp >= 0 and temp <= 12:
    print("Seems to be cold outside. If you go out, wear a jacket!")
    time.sleep(2.4)
    print("I saw that Manor offers some really warm jackets for a discounted price.")
    time.sleep(2.2)
    print(manor["question"])
    manor_answer = input("")
    if manor_answer == "Yes":
        webbrowser.open_new_tab(manor_url)
elif temp >= 13 or temp >= 30:
    print("Oh wow, seems to be nice out there. What are you doing here? Go out!")
    time.sleep(2.6)
    print("Galaxus has some great offers for rubber boats.")
    time.sleep(1.2)
    print(galaxus["question"])
    galaxus_answer = input("")
    if galaxus_answer == "Yes":
        webbrowser.open_new_tab(galaxus_url)
time.sleep(0.5)

# Here the program forwards the user to the manor page or it exits
#if manor_answer == "Yes":
#    webbrowser.open_new_tab(manor_url)
#else:
#    print("Alright, have a good time")
#galaxus_answer == "Yes":
    #webbrowser.open_new_tab(galaxus_url)

# if temp >= 0 and temp <= 12:
    # print("I saw that Manor offers some really warm jackets for a discounted price.")
    # time.sleep(2.8)
    # offer = input("Are you interested?: ")
# elif temp <= 13 or temp <= 30:
    # print("Galaxus has some really great offers for rubber boats.")
    # time.sleep(1.3)
    # offer_galaxus = input("You want to take a look?: ")
