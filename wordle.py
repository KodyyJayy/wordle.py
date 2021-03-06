import os
import random

if os.name != "nt":
	exit()

def get_random_word(file):
	lines = open(file).read().splitlines()
	chosen_word = random.choice(lines)
	return chosen_word

def split_word(word):
	return [char for char in word]

def check_dict(word):
	dict = open('dictionary.txt')
	return (word in dict.read())

letter_place_arr = []
def check_letters(answer_arr, guess_arr):
	current_index = 0

	for letter in guess_arr:
		if guess_arr[current_index] == answer_arr[current_index]: # letter was in correct place
			print(letter + ' +')

		elif letter not in answer_arr: # letter is not in word
			print(letter + ' -')
		else:

			freq_ans = answer_arr.count(letter)
			freq_guess = guess_arr.count(letter)

			if freq_guess > freq_ans: # if letter appears more in guess than in answer

				if  letter_place_arr.count(letter) < freq_guess - 1:
					letter_place_arr.append(letter)
					print(letter + ' -')
				else:
					print(letter + ' /')

			else:

				if letter_place_arr.count(letter) >= freq_ans: # if the current letter is in the array more than the answer
					print(letter + ' -')
				else:
					print(letter + ' /') 
					letter_place_arr.append(letter)

		current_index += 1
	letter_place_arr.clear()

def rematch():
	answer = input('\nPlay again? (y/n): ')

	if answer.lower().strip() == 'y':
		start_game()
	elif answer.lower().strip() == 'n':
		clear_console()
		exit()
	else:
		print('Unknown answer: ' + answer)
		rematch()

def clear_console():
	return os.system('cls')

def start_game():
	clear_console()
	letter_place_arr.clear()
	print('-------------------------------- WORDLE --------------------------------')
	print(' • You get 6 guesses to try guess the word')
	print(' • A minus (-) means the letter is not in the word')
	print(' • A plus (+) means the letter is in the word and in the correct place')
	print(' • A slash (/) means the letter is in the word but not the correct place')
	print('------------------------------------------------------------------------')
	random_word = get_random_word('words.txt')
	answer_arr = split_word(random_word.lower().strip())

	max_rounds = 6
	curr_round = 0

	wrong = '-'
	correct = '+'
	wrong_place = '/'

	guessed_words = []

	while True:
		os.system("title Wordle")
		print('')
		guess = input("Make a guess: ")

		if guess.lower().strip() == random_word.lower().strip():
			clear_console()
			print('Correct!')
			print('You got the word in ' + str(curr_round + 1) + (' tries!' if (curr_round + 1) > 1 else " try!"))
			guess_arr = split_word(guess.lower().strip())
			check_letters(answer_arr, guess_arr)
			rematch()

		if len(guess.strip()) != 5:
			print('Guess must be 5 characters!')
			continue

		if not (guess.strip()).isalpha():
			print('Guess must only contain letters!')
			continue

		if not check_dict(guess.lower().strip()):
			print('Word not found in dictionary!')
			continue

		if guess.lower().strip() in guessed_words:
			print('You already tried this word!')
			continue

		if guess.lower().strip() != random_word.lower().strip():
			curr_round += 1
			print("Incorrect!")
			print("Guesses Remaining: " + str(max_rounds - curr_round))

			guessed_words.append(guess.lower().strip())

			guess_arr = split_word(guess.lower().strip())

			check_letters(answer_arr, guess_arr)

			if curr_round >= max_rounds:
				print('\nGame over, the word was: ' + random_word)
				rematch()

start_game();
