print('Welcome to the shower question chatbot!')
name = input('First, what is your name? ')
age = input(f'Hello {name}, how old are you? ')


def menu():
  print('[1] What is the best legion in Warhammer 40k?') #as
  print('[2] Why can bees fly?')
  print('[3] What is the answer to life, the universe, and everything?')
  print('[4] Exit.')

menu()
option = int(input('Enter the option you would like assistance with.'))

while option != 0:
  if option ==1:
    print('Salamanders! They defend humans, and keep their memories of being a normal human.')
  elif option ==2:
    print('They have wings, and weight surprisingly little.')
  elif option ==3:
    print('42.')
  else:
    print('Invalid Option, choose a digit.')

  print()
  menu()
  option = int(input('Enter the option you would like assistance with.'))
print('Thanks for using this program, goodbye!') 