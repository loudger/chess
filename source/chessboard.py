from figure import King, Queen, Bishop, Knight, Rook, Pawn
from player import Player
from copy import deepcopy


class Chessboard:

	def __init__(self):
		self.tmp_colour_value = 'dark'
		self.board = {}
		for i in range(8,0,-1):
			self.board[str(i)] = dict.fromkeys(['a','b','c','d','e','f','g','h'])
			for let in ['a','b','c','d','e','f','g','h']:
				self.board[str(i)][let] = dict(
					figure='empty',
					colour_space=None
				)

	def play(self):
		'''Цикл с выполнением:
			1.Передача хода
			2.Проверки на возможные ходы
			3.Шах/Мат
			4.Вополнение хода
			5.Игровая логика  (Превращение пешки в ферзя, рокировка и т.д.)
		'''
		pass			

	def connect_player(self, colour_side):
		'''К доске подключается игрок за выбранную сторону
		'''
		Player(colour_side)
		

	def checkup_for_check(self, attack_col, defense_col):
		pass


	def checkup_empty_space(self, num, let):
		'''Проверяет поле находится ли на нём фигура
		'''
		if self.board[num][let] == 'empty':
			return True
		else:
			return False


	def checkup_space_for_move(self, num, let, own_col):
		'''Проверяет может ли туда ходить фигура
		'''
		if self.board[num][let] == 'empty':
			return True
		else:
			if self.board[num][let].colour == own_col:
				return False
			else:
				return True


	# def auxiliary_func_set_colour(self):
	# 	if self.tmp_colour_value == 'dark':
	# 		self.tmp_colour_value = 'ligth'
	# 		return 'ligth'
	# 	else: 
	# 		if self.tmp_colour_value == 'ligth':
	# 			self.tmp_colour_value = 'dark'
	# 		return 'dark'

	def return_figure(self, num, let):
		return self.board[num][let]['figure']


	def return_colour_space(self, num, let):
		return self.board[num][let]['colour']


	# def print(self):
	# 	for i in range (8, -1, -1):
	# 		print (str('-+{}-').format( (('-'*8)+'-+')*8))
	# 		if i != 0:
	# 			print (i, end = '|')
	# 			for let in ['a','b','c','d','e','f','g','h']:
	# 				print (str('{}{}').format(self.board[str(i)][let]['figure'], 
	# 					(lambda x: x.colour[0:1] if x != 'empty' else '')(self.board[str(i)][let]['figure']) ) ,
	# 				end =str(' '*(9-len(self.board[str(i)][let]['figure'].__str__()) - (lambda x: 0 if x == 'empty' else 1 )(self.board[str(i)][let]['figure']))+'|') )
	# 			print()
	# 	print(end = ' |')
	# 	for let in ['a','b','c','d','e','f','g','h']:
	# 		print ( str('    {}    ').format(let) ,end = '|')

	def print(self):
		for i in range (8, -1, -1):
			print (str('-+{}-').format( (('-'*8)+'-+')*8))
			if i != 0:
				print (i, end = '|')
				for let in ['a','b','c','d','e','f','g','h']:
					print (str('{}{}').format(self.board[str(i)][let]['figure'], 
						(lambda x: x.colour[0:1] if x != 'empty' else '')(self.board[str(i)][let]['figure']) ) ,
					end =str(' '*(9-len(self.board[str(i)][let]['figure'].__str__()) - (lambda x: 0 if x == 'empty' else 1 )(self.board[str(i)][let]['figure']))+'|') )
				print()
		print(end = ' |')
		for let in ['a','b','c','d','e','f','g','h']:
			print ( str('{: ^9}').format(let) ,end = '|')

	def filling(self):
		# white
		for let in ['a', 'h']:
			self.board['1'][let]['figure'] = Rook('White')
		for let in ['b', 'g']:
			self.board['1'][let]['figure'] = Knight('White')
		for let in ['c', 'f']:
			self.board['1'][let]['figure'] = Bishop('White')
		self.board['1']['e']['figure'] = King('White')
		self.board['1']['d']['figure'] = Queen('White')
		for let in ['a','b','c','d','e','f','g','h']:
			self.board['2'][let]['figure'] = Pawn('White')
		# # black
		for let in ['a', 'h']:
			self.board['8'][let]['figure'] = Rook('Black')
		for let in ['b', 'g']:
			self.board['8'][let]['figure'] = Knight('Black')
		for let in ['c', 'f']:
			self.board['8'][let]['figure'] = Bishop('Black')
		self.board['8']['e']['figure'] = King('Black')
		self.board['8']['d']['figure'] = Queen('Black')
		for let in ['a','b','c','d','e','f','g','h']:
			self.board['7'][let]['figure'] = Pawn('Black')


	def move_from_to(self, from_coord, to_coord):
		'''
		from_coord, to_coord = [['1'],['a']]
		''' 
		if self.board[from_coord[0][0]][from_coord[1][0]]['figure'].untouched: 
			self.board[from_coord[0][0]][from_coord[1][0]]['figure'].touch()
		self.board[to_coord[0][0]][to_coord[1][0]]['figure'] = self.board[from_coord[0][0]][from_coord[1][0]]['figure']
		self.board[from_coord[0][0]][from_coord[1][0]]['figure'] = 'empty'
	


a = Chessboard()
a.filling()
a.print()

while True:
	
	print()
	l = input('Введите откуда столбец:')
	n = input('Введите откуда строку:')
	l1 = input('Введите куда столбец:')
	n1 = input('Введите куда строка:')
	a.move_from_to([[n],[l]],[[n1],[l1]])
	print('\n'*2)
	a.print()
	# print(id(a.board['1']['a']))
	# print(id(a.board['1']['b']))

	# print(a.board)
