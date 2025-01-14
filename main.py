print('Welcome to the random question chatbot!')
name = input('What is your name?')
age = input('How old are you?')

def menu():
    print('[1] Can bees fly?')
    # yes
    print('[2] Best loyalist space marine chapter in Warhammer 40k?')
    # salamanders!
    print('[3] Who let the dogs out?')
    # baha men
    print('[4] Exit.')

menu()
option = int(input('Enter your option: '))

while option != 4:
    if option == 1:
        print('Somehow, they can.')
    elif option == 2:
        print('Salamanders!')
    elif option == 3:
        print('The baha men.')
    else:
        print('Choose another option.')

    print()
    menu()
    option = int(input('Enter your option: '))
print('Thank you for using our program. Goodbye!')