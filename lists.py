fruits = ["Apples", "Ananas", "Banana", "Avocado"]
First2Fruits = fruits[0:2]
print(First2Fruits)
print(fruits[:])


for i in range(len(fruits)):
    print("Index " + str(i) + " in fruits is: " + fruits[i])

fruits.index("Ananas")
