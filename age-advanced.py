age1 = int(input("Tell me your age: "))
age2 = int(input("Tell me your friends age: "))

if(age1 >= 18 and age2 >= 18):
    print('\x1b[0;32;44m' + "You are both adults" '\x1b[0m')
elif(age1 > 17 or age2 > 17):
    print('\x1b[1;35;47m' + "One age is 18 or higher" + '\x1b[0m')
else:
    print('\x1b[1;37;42m' + "You are both children" + '\x1b[0m')
