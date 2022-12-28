import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses

def generate_response(user_input):
  responses = [
    "anything else?",
    "One of my favorites!",
    "One of the best here."
  ]
  return random.choice(responses)
def init_chat():
  quit_character = 'that is all'

  user_input = input("Hello, Welcome to Fred's Cuisine! How can I get you started?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()