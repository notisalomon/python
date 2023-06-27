import time

question1 = {
	"question": "What is the capital of France?",
	"choices": ["A. Paris", "B. London", "C. Berlin"],
	"answer": "A"
}

time.sleep(0.5)
# Print the question and answer choices
print(question1["question"])
time.sleep(0.9)
for choice in question1["choices"]:
        print(choice)

time.sleep(0.5)

# Ask the user to select an answer
user_answer = input("Enter your answer (A, B or C): ")

time.sleep(0.5)

# Check if the answer is correct
if user_answer == question1["answer"]:
	print('\x1b[1;32;40m' + "Correct" + '\x1b[0m')
else:
	print('\x1b[1;31;40m' + "Sorry, that's incorrect." + '\x1b[0m')
time.sleep(0.6)
