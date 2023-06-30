import time
import sys

question1 = {
        "question":"Are you hungry?",
        "choices": ["Yes", "No"]
    }

question2 = {
        "question":"What would you like to eat?",
        "choices":["A. Hamburger", "B. Pizza", "C. Lasagne"]
        }

print(question1["question"])
time.sleep(0.6)
for choice in question1["choices"]:
    print(choice)
time.sleep(0.3)
is_hungry = input("Enter your answer (Yes or No): ")
time.sleep(0.4)
if is_hungry == "Yes" or is_hungry == "yes":
    print("Good, what do you want to eat?")
else:
    sys.exit("Aaah, i could have cooked you something delicious..")
time.sleep(1)
for choice in question2["choices"]:
    print(choice)
time.sleep(0.1)
user_answer = input("Enter your answer (A, B or C): ")
time.sleep(0.5)
if user_answer == "A" or user_answer == "Hamburger" or user_answer == "a" or user_answer == "hamburger":
    print("mmmm.. Nothing better than a classical american hamburger!")
elif user_answer == "B" or user_answer == "b" or user_answer == "Pizza" or user_answer == "pizza":
    print("Aaah.. Bella Italia. Good choice!")
else:
    print("Who doesn't like Lasagne?")
time.sleep(2)
