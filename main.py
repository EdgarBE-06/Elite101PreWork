name = input("Greetings user what is your name? " )
age = input(f'So {name} how old are you ')
option1 = 'placeholder1'
option2 = 'placeholder2'
option3 = 'placeholder3'
option4 = 'placeholder4'
def help():
  help = input(f'Do you need help with {option1}, {option2}, {option3},or {option4} ')
  if help == option1:
    print('How can I help you with that.')
  elif help == option2:
    print('How can I help you with that.')
  elif help == option3:
    print('How can I help you with that.')
  elif help == option4:
    print('How can I help you with that.')
  elif help == 'no':
    print("Okay goodbye.")
  else:
    print("I'm sorry I can't help you with that.")

help()