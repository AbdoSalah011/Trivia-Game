# Import the random module to shuffle the questions and options
import random

# Define a list of questions, each with a question, four options, and an answer
questions = [
  {
    "question": "What is the capital of Egypt?",
    "options": ["Cairo", "Alexandria", "Luxor", "Aswan"],
    "answer": "Cairo"
  },
  {
    "question": "Who wrote the Harry Potter series?",
    "options": ["J.R.R. Tolkien", "George R.R. Martin", "J.K. Rowling", "C.S. Lewis"],
    "answer": "J.K. Rowling"
  },
  {
    "question": "Which planet is the second largest in the solar system?",
    "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
    "answer": "Saturn"
  },
  {
    "question": "What is the name of the phobia that means fear of spiders?",
    "options": ["Arachnophobia", "Acrophobia", "Agoraphobia", "Claustrophobia"],
    "answer": "Arachnophobia"
  },
  {
    "question": "Which country won the 2018 FIFA World Cup?",
    "options": ["France", "Croatia", "Brazil", "Germany"],
    "answer": "France"
  }
]

# Shuffle the questions
random.shuffle(questions)

# Initialize the score to zero
score = 0

# Loop through the questions
for question in questions:
  # Print the question
  print(question["question"])
  # Shuffle the options
  random.shuffle(question["options"])
  # Print the options with numbers
  for i in range(4):
    print(f"{i+1}. {question['options'][i]}")
  # Ask the user to enter their answer
  answer = input("Enter your answer (1, 2, 3, or 4): ")
  # Check if the answer is valid
  if answer.isdigit() and 1 <= int(answer) <= 4:
    # Check if the answer is correct
    if question["options"][int(answer) - 1] == question["answer"]:
      # Print a positive feedback
      print("Correct!")
      # Increase the score by one
      score += 1
    else:
      # Print a negative feedback
      print("Wrong!")
      # Print the correct answer
      print(f"The correct answer is {question['answer']}")
  else:
    # Print an invalid input message
    print("Invalid input. Please enter a number between 1 and 4.")
  # Print a blank line
  print()

# Print the final score
print(f"Your final score is {score} out of {len(questions)}")