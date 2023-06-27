question1 = {
	"question": "What is the capital of France?",
	"choices": ["A. Paris", "B. London", "C. Berlin"],
	"answer": "A"
}

# Print the question and answer choices
print(question1["question"])
for choice in question1["choices"]:
        print(choice)

# Ask the user to select an answer
user_answer = input("Enter your answer (A, B or C): ")

# Check if the answer is correct
if user_answer == question1["answer"]:
	print("Correct")
else:
	print("Sorry, tha'ts incorrect.")

