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

temp = int(input("How many degrees is the temperature today?: "))
time.sleep(0.4)
if temp >= 0 and temp <= 12:
    print("Seems to be cold outside. If you go out, wear a jacket!")
    time.sleep(2.4)
    print("I saw that Manor offers some really warm jackets for a discounted price.")
    time.sleep(2.2)
    print(manor["question"])
    manor_answer = input("")
    if manor_answer == "Yes" or manor_answer == "yes":
        webbrowser.open_new_tab(manor_url)
    elif manor_answer == "No" or manor_answer == "no":
        time.sleep(0.3)
        print("Okay, just wear good clothes!")
elif temp >= 13 or temp >= 30:
    print("Oh wow, seems to be nice out there. What are you doing here? Go out!")
    time.sleep(2.4)
    print("Galaxus has some great offers for rubber boats.")
    time.sleep(2.2)
    print(galaxus["question"])
    galaxus_answer = input("")
    if galaxus_answer == "Yes" or galaxus_answer == "yes":
        webbrowser.open_new_tab(galaxus_url)
    elif galaxus_answer == "No" or galaxus_answer == "no":
        time.sleep(0.3)
        print("Okay, enjoy the weather!")
time.sleep(0.7)
