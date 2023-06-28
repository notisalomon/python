secret_number = 5
guess = int(input("Guess a number: "))
while guess != secret_number:
    guess = int(input("Guess a number: "))
else:
    print('\x1b[1;32;40m' "Congratulations, you got it!" '\x1b[0m')
