#Building a multiple choice quiz
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    

#Classes and Objects
#class Student:
#    def __init__(self, name, major, gpa, is_on_probation):
#        self.name = name
#        self.major = major
#        self.gpa = gpa
#        self.is_on_probation = is_on_probation

#Writing to files
#employee_file = open("index.html", "w")
#employee_file.write("<p>This is HTML</p>")
#employee_file.close()

#Reading Files
#employee_file = open("employees.txt", "r")
#for employee in employee_file.readlines():
#    print(employee)
#employee_file.close()

#try and expect
#try:
#    value = 10/0
#    number = int(input("Enter a number: "))
#    print(number)
#except ZeroDivisionError as err:
#    print(err)
#except ValueError as err:
#    print(err)


#Translator
#def translate(phrase):
#    translation = ""
#    for letter in phrase:
#        if letter.lower() in "aeiou":
#            if letter.isupper():
#                translation = translation + "G"
#            else:
#                translation = translation + "g"
#        else:
#            translation = translation + letter
#    return translation
#print(translate(input("Enter a phrase: ")))

#2d Lists and Nested For Loops
#number_grid = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [0]
#]
#print(number_grid[2][0])
#for row in number_grid:
#    for col in row:
#        print(col)

#Exponent Function
#def raise_to_power(base_num, pow_num):
#    result = 1
#    for index in range (pow_num):
#        result = result * base_num
#    return result
#print(raise_to_power(3, 4))

#For Loop
#friends = ["Jim", "Karen", "Kevin"]
#for index in range(5):
#    if index == 0:
#        print("first Iteration")
#    else:
#        print("Not first")

#Building a Guessing Game
#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False
#while guess != secret_word and not(out_of_guesses):
#    if guess_count < guess_limit:
#        guess = input("Enter guess: ")
#        guess_count += 1
#    else:
#        out_of_guesses = True
#if out_of_guesses:
#    print("Out of Guesses, YOU LOOSE!")
#else:
#    print("You win!")

#while loops
#i = 1
#while i <= 10:
#    print(i)
#    i += 1
#
#print("Done with loop")

#Dictionaries
#monthConversions = {
#    "Jan": "January",
#    "Feb": "February",
#    "Mar": "March",
#    "Apr": "April",
#    "May": "May",
#    "Jun": "June",
#    "Jul": "July",
#    "Aug": "August",
#    "Sep": "September",
#    "Oct": "October",
#    "Nov": "November",
#    "Dec": "December",
#}
#print(monthConversions.get("Luv", "Not a valid Key"))

#Advanced Calculator
#num1 = float(input("Enter first number: "))
#op = input("Enter operator: ")
#num2 = float(input("Enter second number: "))
#if op == "+":
#    print(num1 + num2)
#elif op == "-":
#    print(num1 - num2)
#elif op == "/":
#    print(num1 / num2)
#elif op == "*":
#    print(num1 * num2)
#else:
#    print("Invalid Operator")

#if statements and comparisons
#def max_num(num1, num2, num3):
#    if num1 >= num2 and num1 >= num3:
#        return num1
#    elif num2 >= num1 and num2 >= num3:
#        return num2
#    else:
#        return num3
#print(max_num(3, 5, 987))

#if statements
#is_male = True
#is_tall = True
#if is_male and is_tall:
#    print("You are a tall male")
#elif is_male and not(is_tall):
#    print("You are a short male")
#elif not(is_male) and is_tall:
#    print("You are nota a male but are tall")
#else:
#    print("You are either not male or not tall or both")



#def cube(num):
#    return num*num*num
#result = cube(4)
#print(result)

#Functions
#def say_hi(name, age):
#    print("Hello " + name +", you are " + str(age) + " years old.")
#say_hi("Labi", 35)

#Tuples
#coordinates = [(4, 5), (6, 7), (8, 9)]
#print(coordinates[0][1])

#Lists & Lists Functions
#friends = ["Kevin", "Karen", "Jim", "Suzana"]
#friends[1] = "Mike"
#friends.remove("Kevin")
#print(friends.index("Mike"))
#friends.sort()
#print(friends)
#friends2 = friends.copy()
#print(friends2)


#Madlip Game
#color = input("Enter a color: ")
#plural_noun = input("Enter a Plural Noun: ")
#celebrity = input("Enter a celebrity: ")
#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)

#Calculator
#num1 = float(input("Enter a number: "))
#num2 = float(input("Enter another number: "))
#result = num1 + num2
#print(result)


#User Inputs + Variables
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name + "! You are " + age + " years old!")

#Working with Numbers
#from math import *
#my_num=-5
#print(sqrt(36))
#print(ceil(2.1))
#print(min(4, 6, 5, 9, 12, 1))
#print(str(my_num) + " is my favorite number!")

#Working with Strings
#phrase = "Giraffe Academy"
#print(phrase.replace("Giraffe", "Majmun"))
#print(phrase.index("A"))
#print(phrase[1])
#print(len(phrase))
#print(phrase.upper())


#Variables and Data types
#character_name = "Labi"
#age = "28"
#is_male = True

#print("There once was a man named " + character_name + ",")
#print("he was " + age + " years old. ")
#character_name = "Toni"
#print("He really liked the name " + character_name + ",")
#print("but didn't like being " + age + ".")