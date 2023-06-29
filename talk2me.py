import time

name = input("Hi! What's your name? ")
time.sleep(0.7)
print("Nice to meet you " + name)
time.sleep(0.6)
input("How are you today? ")
time.sleep(0.6)
input("How is your Diet going so far? ")
time.sleep(0.6)
print("You look great anyways! Was just wondering.")
time.sleep(1.8)
input("Have you ever wondered why apples are red and bananas are purple? ")
time.sleep(0.6)
age = int(input("Anyway, how old are you " + name + "? "))
time.sleep(0.6)
if age < 18:
    print("Wait. Am i talking to a child?")
elif age == 18:
    print("oooh, you just turned 18 recently. Welcome to the real world ;)")
else:
    print("No way, i thought you were much younger.")
time.sleep(1.8)
print("So " + name + ", why are you wasting your time with a computer program?")
time.sleep(3)
