#Eva D.
#P1. 01/24/25
#Magic 8 Ball List


#init
"""
Requirements:
Create a list variable named responses to store a set of at least 15 predefined responses.
Use the random.choice() function to select a random response from the responses list.
Prompt the user to enter a yes-or-no question and store it in a variable.
Validate the user's input to ensure it ends with a question mark. If not, ask the user to re-enter the question.
Generate and display a random response from the responses list.
Ask the user if they want to ask another question.
Repeat the process if the user responds with "yes" or "y" and exit the program if the user responds with "no" or "n".
"""

#functions
import random

responses = [
    "Yes", "No", "Maybe", "Ask again later", "Definitely",
    "I don't think so", "Absolutely", "Not sure", "Try again",
    "Most likely", "Unlikely", "No doubt about it", "Better not tell you now",
    "Cannot predict now", "Outlook good"
]

def magic_8_ball():
    last_response = None  #this prevents the 8 ball from repeating answers

    while True:
        # Ask for a question
        question = input("Ask a yes-or-no question: ")

        if '?' not in question:
            print("Please make sure your question ends with '?'")
            continue  # If not, ask again

        # Get a random response
        response = random.choice(responses)
        while response == last_response:
            response = random.choice(responses)

        print("Magic 8 Ball says:", response)
        last_response = response

        #ask user if they wanna go again
        again = input("Ask another question? (yes or no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

#main
magic_8_ball()
