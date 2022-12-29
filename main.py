import random

special = ['fish fillet', 
           'crab rangoon', 
           'lobster', 
           'lobster mac n cheese'
          ]
reservations = ['Monday-4 PM',
                'Tuesday-3 PM'
                'Wednesday-8 PM']

def generate_response(user_input):
  responses = [
    "anything else?",
    "One of my favorites! Is there anything else?",
    "One of the best here. Is there anything else I could get you?"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = "that is all"

  user_input = input("Hello, Welcome to Fred's Cuisine! How can I get you started?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    if user_input == 'water':
      user_input = input('ok, anything else? \n')
    elif user_input == 'special menu':
      print("our special today:")
      print(special)
      user_input = input('ok, what else? \n')
    elif user_input == 'reservations':
      print('These are our availible hours')
      print(reservations)
      user_input = input('Do you need anything else?')
    else :  
      user_input = input(generate_response(user_input) + "\n")


  
if __name__ == "__main__":
  init_chat()
