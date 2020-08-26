'''
Write a program that simulates a fortune cookie. The program
should display one of five unique fortunes, at random, each
time it's run.
'''
import random
fortunes = ["Don't be afraid. Be focused.",
            'Children really brighten up a household', 'Congratulations! today is your day', 'Emotional empathy is what motivates us to help others']
random_fortune_index = random.randrange(len(fortunes))
print(fortunes[random_fortune_index])

'''
Write a program that flips a coin 100 times and then tells you
the number of heads and tails.
'''
number_of_head = 0
number_of_tail = 0
number_of_times_flipped = 100

while number_of_times_flipped:
    random_int = random.randint(1, 2)
    if (random_int % 2) == 0:
        number_of_head += 1
    else:
        number_of_tail += 1

    number_of_times_flipped -= 1

print('number of tail is', number_of_tail, 'number of head is', number_of_head)
