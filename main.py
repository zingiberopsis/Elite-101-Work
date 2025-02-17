problem 1
#Write a program that takes a phrase or sentence as INPUT (e.g., "Federal Bureau of Investigation") and generates the corresponding acronym (e.g., "FBI"). The acronym should be formed by taking the first letter of each word and converting it to uppercase.



def generate_acronym(phrase): #generate acronym
  acronym = ""
  for word in phrase.split():  # split words
    acronym += word[0].upper()  #acapitalize first lette of each owrd
  return acronym

# Example usage
phrase = "Random access memory"
print(generate_acronym(phrase))  #ouput: "RAM"

#problem 2
#Create a program that first asks the user which temperature scale they would like to convert from (e.g., Celsius, Fahrenheit, Kelvin). Then, ask which temperature scale they would like to convert to. Afterward, PROMPT the user for the temperature value and perform the CONVERSION. (math)
def convert_temperature():
    """
    Prompts the user for the initial temperature scale, desired conversion scale, and temperature value, then performs the conversion and prints the result.
    """
    from_temp_type = input("Enter the temperature scale to convert from (C for celsius, F for fahrenheit, K for kelvin: ").upper()
    to_scale = input("Enter the temperature scale to convert to (C for celsius, F for fahrenheit, K for kelvin): ").upper()
    temp_value = float(input("Enter the temperature value: "))

    if from_temp_type
        if to_scale == 'F':
            converted_temp = (temp_value * 9/5) + 32
        elif to_scale == 'K':
            converted_temp = temp_value + 273.15
        else:
            print("Invalid conversion choice.")
            return
    elif from_temp_type
        if to_scale == 'C':
            converted_temp = (temp_value - 32) * 5/9
        elif to_scale == 'K':
            converted_temp = (temp_value - 32) * 5/9 + 273.15
        else:
            print("Invalid conversion choice.")
            return
    elif from_temp_type == 'K':
        if to_scale == 'C':
            converted_temp = temp_value - 273.15
        elif to_scale == 'F':
            converted_temp = (temp_value - 273.15) * 9/5 + 32
        else:
            print("Invalid conversion choice.")
            return
    else:
        print("Invalid input for initial temperature scale.")
        return

    print(f"{temp_value} degrees {from_temp_typ } is equal to {converted_temp:.2f} degrees {to_scale}")

if __name__ == "__main__":
    convert_temperature()

#problem 3

#Create a function that, given a sentence, determines the longest word and RETURNs it. If there are multiple words of the same maximum length, RETURN the FIRST one that appears in the sentence.
def longest_word(sentence:)
    words = sentence.split()
    longest = ''
    for word in words: #sentence
        if len(word) > len(longest) #len = length
        longest = word# ^also checks current word for length (being longest or not)
    return longest #only toldt o return

#problem 4

#Write a program that lets the user play a single round of Rock, Paper, Scissors against the computer. The computer should RANDOMly choose one of the three OPTIONs, and then the user will be prompted for their choice. The program then announces the result (win, lose, or draw).

import random

def rock_paper_scissors_game():
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)
    user_choice = input('Choose either Rock, Paper, or Scissors: ').lower()

    print(f'You chose {user_choice}. The opponent chose {computer_choice}.')

    if user_choice == computer_choice:
        print ('It's a tie!')
    elif (user_choice == 'rock' and computer choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        print('You win!')
    else:
        print('You lose!')

rock_paper_scissors_game()
# i wish i had enough energy to separate the problems into different files
# but i dont, due to it being about 3 am. i hope this is fine! sorry for the inconvenience!
# reason i didnt have time was due to being gone ALL weekend, and having to do this all in a few hours.
