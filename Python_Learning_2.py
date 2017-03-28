import curses
from random import randrange,choice
from collections import defaultdict


actions=['Up','Down','Left','Right','Restart'.'Exit']
letter_codes=[ord(ch) for ch in 'WASDRQwasdrq']
actions_dict=dict(zip(letter_codes,actions*2))

def main(stdscr):
	

	def init():
		return 'Game'

	def not_game(state):
		
		response = defaultdict(lambda:states)
		response['Restart'],response['Exit']='Init','Exit'
		return response[states]

	def game():
		

		if action='Restart':
			return 'Init'

		if action=='Exit':
			return 'Exit'

			if 游戏胜利了:
				return 'Win'

			if 游戏失败了:
				return 'Gameover'

		return 'Game'

	state_actions={
		'Init':init,
		'Win':lambda:not_game('Win'),
		'Gameover':lambda:not_game('Gameover'),
		'Game':game
	}	

	while state != 'Exit':
		state = state_actions[state]()


def get_user_action(keyboard):
	char='N'
	while char not in actions_dict:
		char=keyboard.getch()
	return actions_dict[char]

def transpose(field):
	return [list(row) for row in zip(*field)]

def invert(field):
	return [row[::-1] for row in field]

class GameField(object):
	
	def __init__(self, height=4,width=4,win=2048):
		# super(GameField, self).__init__()
		self.height = height
		self.width = width
		self.win_value = win
		self.score=0
		self.highscore =0
		self.reset()


	def spawn(self):
		new_element=4 if randrange(100) > 89 else 2
		(i,j)=choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j]==0]
		self.field[i][j]=new_element

	def resst():
		if self.score>self.highscore:
			self.highscore=self.score
		self.score=0
		self.field=[[0 for i in range(self.width)] for j in range(self.height)]
		self.spawn()
		self.spawn()

	def function():
		pass

	