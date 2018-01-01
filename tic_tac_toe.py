# Python Boot Camp Milestone Project 1
# Neville Bergin orginal solution 28/12/17
import random # This is required for the coin toss to decide who goes first
import os # Will be used to issue a command to clear the screen
import time #Will be used to delay actions using sleep()

win = False

# Add some Titles

print('T' *5, ' ' * 1, 'I'*3, ' ' *2, 'C' *2)
print(' ' * 1,'T' *1, ' ' * 4, 'I'*1, ' ' *2, 'C' *1, ' ' *1, 'C' *1)
print(' ' * 1,'T' *1, ' ' * 4, 'I'*1, ' ' *2, 'C' *1)
print(' ' * 1,'T' *1, ' ' * 4, 'I'*1, ' ' *2, 'C' *1, ' ' *1, 'C' *1)
print(' ' *1,'T' *1,' ' * 3, 'I'*3, ' ' *2, 'C' *2)
print('\n')
print('T' *5, ' ' * 2, 'A'*2, ' ' *5, 'C' *2)
print(' ' * 1,'T' *1, ' ' * 2, 'A' *1, ' ' *2, 'A' *1,' ' *1, 'C' *1,' ' *1,'C' *1)
print(' ' * 1,'T' *1, ' ' * 2, 'A' *1, ' ' *2, 'A' *1,' ' *1, 'C' *1)
print(' ' * 1,'T' *1, ' ' * 2, 'A' *6, ' ' *1, 'C' *1, ' ' *1, 'C' *1)
print(' ' *1,'T' *1,' ' * 2, 'A' *1, ' ' *2,'A' *1,' ' *3, 'C' *2)
print('\n')
print('T' *5, ' ' * 2, 'O'*2, ' ' *3, 'E' *5)
print(' ' * 1,'T' *1, ' ' * 2, 'O' *1, ' ' *2, 'O' *1,' ' *1, 'E' *1)
print(' ' * 1,'T' *1, ' ' * 2, 'O' *1, ' ' *2, 'O' *1,' ' *1, 'E' *3)
print(' ' * 1,'T' *1, ' ' * 2, 'O' *1, ' '*2,'O' *1, ' ' *1, 'E' *1)
print(' ' *1,'T' *1,' ' * 4, 'O' *2,' ' *3, 'E' *5)
print('\n')
print('Neville Bergin')
print('28/12/17')
print('\n'*3)
print('_'*29)
print('This is a game for two players')
print('\n')

board ={'A1':' ' , 'A2':' ' , 'A3':' ' , 'B1':' ' ,'B2':' ' ,'B3':' ', 'C1':' ' ,'C2':' ' ,'C3':' '}

def player_details():# Each player enters their name which are stored in the variables player1 and player2
	global player1
	player1 = input('Player 1, what is your name? ')
	print('Welcome  ' + player1)
	print('\n')
	global player2
	player2 = input('Player 2, what is your name? ')
	print('Welcome  ' + player2)
	os.system('cls') # Clears screen
	


def coin_toss():
	global first_player, second_player
	print('\n')
	print('\n')
	print("Ok, let's begin by tossing a coin to see who will go first!!")
	print('_'*29)
	print('\n\n')
	toss = random.randint(1,2)
	if toss == 1:
		first_player = player1
		second_player = player2
	else:
		first_player = player2
		second_player = player1
	print(first_player, 'you will be going first')
	print('\n')
	print('\n')
	print('Here is the board. The squares are referenced by letter first, then number thus: B2, followed by the Enter key')
	print('\n')
	print('\n')




def clear_board():
	global board
	board ={'A1':' ' , 'A2':' ' , 'A3':' ' , 'B1':' ' ,'B2':' ' ,'B3':' ', 'C1':' ' ,'C2':' ' ,'C3':' '}



def board_status():  # A function to print the board at any time
	print(' '*3,'1', ' '*3,'2',' '*3,'3')
	print(' ','*'*19)
	print(' ','*',' '*3,'*',' '*3,'*',' '*3,'*',' '*3)
	print('A','*','',board['A1'],'','*','',board['A2'],'','*','',board['A3'],'','*')
	print(' ','*',' '*3,'*',' '*3,'*',' '*3,'*',' '*3)
	print(' ','*'*19)
	print(' ','*',' '*3,'*',' '*3,'*',' '*3,'*',' '*3)
	print('B','*','',board['B1'],'','*','',board['B2'],'','*','',board['B3'],'','*')
	print(' ','*',' '*3,'*',' '*3,'*',' '*3,'*',' '*3)
	print(' ','*'*19)
	print(' ','*',' '*3,'*',' '*3,'*',' '*3,'*',' '*3)
	print('C','*','',board['C1'],'','*','',board['C2'],'','*','',board['C3'],'','*')
	print(' ','*',' '*3,'*',' '*3,'*',' '*3,'*',' '*3)
	print(' ','*'*19)


	
def select_square(): # Function to get users to select the square they wish to place their mark in
	
	selection = str.upper(input('Enter the reference of the cell that you want to select:  '))
	if board[selection] != ' ':
		print('\n\t That square is already occupied')
		selection = ''
		time.sleep(2)
		os.system('cls')
		board_status()
		select_square()
	if player == first_player:
		marker = 'X'
	else:
		marker = 'O'
	board[selection] = marker
	test_win()
	os.system('cls')
	board_status()
	test_no_moves()

def test_win(): # Test to see if the move has resulted in a win, check horiz, vert and diag
	global win
	win = False
	if all(x ==' ' for x in board.values()) == True:
		win = False
	elif board['A1'] != ' ' and board['A1'] == board['A2'] and board['A2'] == board['A3']:
		 win = True
	elif board['B1'] != ' ' and board['B1'] == board['B2'] and board['B2'] == board['B3']:
		win = True
	elif board['C1'] != ' ' and board['C1'] == board['C2'] and board['C2'] == board['B3']:
		win = True
	elif board['A1'] != ' ' and board['A1'] == board['B1'] and board['B1'] == board['C1']:
		win = True
	elif board['A2'] != ' ' and board['A2'] == board['B2'] and board['B2'] == board['C2']:
		win = True
	elif board['A3'] != ' ' and board['A3'] == board['B3'] and board['B3'] == board['C3']:
		win = True
	elif board['A1'] != ' ' and board['A1'] == board['B2'] and board['B2'] == board['C3']:
		win = True
	elif board['A3'] != ' ' and board['A3'] == board['B2'] and board['B2'] == board['C1']:
		win = True
	else:
		win = False
	if win == True:
		os.system('cls')
		board_status()
		congrats()

def test_no_moves(): # test to make sure there are still moves left available
	if all(y == 'X' or  y == 'O' for y in board.values() ) == True:
		moves = False
	else:
		moves = True
		
	if moves == False:
		no_more_moves()
		
		
def no_more_moves(): # Let players know that there are no more moves available
	no_move = str.upper(input('\tThere are no more moves possible, the game is drawn. Would you like to play again Y or N?  '))
	if no_move == 'Y':
		player_details()
	else:
		end_game()
	
	
	
def end_game(): # Clear the screen and say thank you!
	os.system('cls')
	board_status()
	print('\n\n\tThank you both for playing. See you next time!')
	quit()
	
		
def play_again(): # Check if the players would like to play again
	play = str.upper(input('\t Would you like to play again Y or N?  '))
	if play == 'Y':
		clear_board()
		os.system('cls')
		board_status()
		player_details()
	else:
		os.system('cls')
		board_status()
		end_game()

def congrats(): # Prints a congratulations message
	print('\n\n\t Congratulations ' + player + ' you have won!')
	play_again()
	

	
def game_flow(): # This function should control the progress of the game and cycle through both players until we have a winner
	player_details()
	coin_toss()
	board_status()
	while win == False:
		global player
		player = first_player
		print(first_player +'  select a square')
		select_square()
		print(second_player +'  select a square')
		player = second_player
		select_square()
		

game_flow()



