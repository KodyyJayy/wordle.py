import os
import random

def get_random_word(file):
	lines = open(file).read().splitlines()
	randline = random.choice(lines)
	#print(randline)
	return randline

def split_word(word):
	return [char for char in word]

def check_dict(word):
	dict = open('dictionary.txt')
	return (word in dict.read())

letter_place_arr = []
def check_letters(answer_arr, guess_arr):
	#print(guess_arr)
	#print(answer_arr)

	current_index = 0

	for letter in guess_arr:
		if guess_arr[current_index] == answer_arr[current_index]: #letter was in correct place
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

				if letter_place_arr.count(letter) >= freq_ans:
					print(letter + ' -')
				else:
					print(letter + ' /')
					letter_place_arr.append(letter)

		current_index += 1
	letter_place_arr.clear()

def rematch():
	answer = input('Play again? (y/n): ')

	if answer.lower() == 'y':
		start_game()
	elif answer.lower() == 'n':
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
	print(' • A minus (-) means the letter is not in the word')
	print(' • A plus (+) means the letter is in the word and in the correct place')
	print(' • A slash (/) means the letter is in the word but not the correct place')
	print('------------------------------------------------------------------------')
	print(' ')
	randomWord = get_random_word('words.txt')
	answer_arr = split_word(randomWord.lower())

	max_rounds = 6
	curr_round = 0

	wrong = '-'
	correct = '+'
	wrong_place = '/'

	guessed_words = []

	while True:

		guess = input("Make a guess: ")

		if guess.lower() == randomWord.lower():
			clear_console()
			print('You win!')
			guess_arr = split_word(guess.lower())
			check_letters(answer_arr, guess_arr)
			rematch()

		if len(guess) != 5:
			print('Guess must be 5 characters!')
			continue

		if not guess.isalpha():
			print('Guess must only contain letters!')
			continue

		if not check_dict(guess.lower()):
			print('Word not found in dictionary!')
			continue

		if guess in guessed_words:
			print('You already tried this word!')
			continue

		if guess != randomWord:
			curr_round += 1
			print("Incorrect!")
			print("Guesses Remaining: " + str(max_rounds - curr_round))

			guessed_words.append(guess.lower())

			guess_arr = split_word(guess.lower())

			check_letters(answer_arr, guess_arr)

			if curr_round >= max_rounds:
				print('Game over, the word was: ' + randomWord)
				rematch()

	start_game();

start_game();