'''
Write a program that counts for the user. Let the user enter the
starting number, the ending number, and the amount by which
to count
'''
start_num = int(input('Enter starting number: '))
end_num = int(input('Enter ending number: '))
step_num = int(input('Enter amount to step by: '))
for number in range(start_num, end_num, step_num):
    print(number)

'''
Create a program that gets a message from the user and then
prints it out backwards
'''
user_message = input('Enter your message: ')
reversed_message = ''
stringlength = len(user_message)
# first approach
for character in range(stringlength - 1, -1, -1):
    reversed_message += user_message[character]

print(reversed_message)
# second approcach
reversed_message = user_message[stringlength::-1]
print(reversed_message)

'''
Create a game where the computer picks a random word and
the player has to guess that word. The computer tells the
player how many letters are in the word. Then the player gets
five chances to ask if a letter is in the word. The computer can
only respond with “yes” or “no”. Then, the player must guess
the word
'''
import random
list_of_words = ('player', 'awesomeness', 'bass', 'randoms')
number_of_chances = 5
random_word_index = random.randint(0, len(list_of_words)-1)
random_word = list_of_words[random_word_index]
player_guess = input('I am thinking of a word, can you guess it? ')

while number_of_chances != 0:
    if player_guess == random_word:
        print('Wow, genius. You got it right.')
        break
    else:
        number_of_chances -= 1
        print('Nope, you are wrong')
        print('The word has', len(random_word), 'letters')
        print('You have ', number_of_chances, 'chances left')
        player_guess = input('I am thinking of a word, can you guess it? ')
print('The guess was', random_word)
