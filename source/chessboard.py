from figure import King, Queen, Bishop, Knight, Rook, Pawn
from player import Player

class Chessboard():

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

	def run(self):
		'''Цикл с выполнением:
			1.Передача хода
			2.Проверки на возможные ходы
			3.Шах/Мат
			4.Вополнение хода
			5.Игровая логика  (Превращение пешки в ферзя, рокировка и т.д.)
		'''
		pass


	def pawn_possibilities_moves(self,src_coord):
		'''src_coord = ['1','a']
		Эта функция должна по координатам пешки определять её возможные ходы
		Используя при этом вспомогательную функцию пешки, которая выдаёт абсолютно все ходы, не смотря на остальные фигуры
		Данный метод проходится отдельно по первой части untested_cells(которая указывает на ходы вперед)
		и на вторую часть untested_cells(которая указывает на поле по диагонали, где можно съесть фигуру)

		Например он проходит по линии впереди и если там будет фигура, то добавлять все дальнейшие клетки в лист для удаления
		А потом просто удалит все элементы из основного листа возможных ходов
		'''
		untested_cells = self.return_figure(src_coord).untested_possible_moves(src_coord)
		if not untested_cells[0]:
			pass
		else:
			remove_flag = False
			remove_list = []
			for dest_coord in untested_cells[0]:
				if self.return_figure(dest_coord) != 'empty' or remove_flag:
					remove_flag = True
					remove_list.append(dest_coord)
			for remove_coord in remove_list:
				untested_cells[0].remove(remove_coord)
		remove_list = []
		for dest_coord in untested_cells[1]:
			if self.return_figure(dest_coord) == 'empty' or self.return_colour_figure(dest_coord) == self.return_figure(src_coord):
				remove_list.append(dest_coord)
		for remove_coord in remove_list:
			untested_cells[1].remove(remove_coord)
		return untested_cells


	def brq_possibilities_moves(self, src_coord):
		''' Проходит по всем линиям и говорит где можно где нельзя вставать
		Одна идея для Ладей, Слонов, Королев'''
		untested_cells = self.return_figure(src_coord).untested_possible_moves(src_coord)
		for line in untested_cells:
			if line:
				remove_flag = False
				remove_list = []
				for dest_coord in line:
					if remove_flag:
						remove_list.append(dest_coord)
					elif self.return_figure(dest_coord) != 'empty':
						remove_flag = True
						if self.return_colour_figure(dest_coord) == self.return_colour_figure(src_coord):
							remove_list.append(dest_coord)
				for remove_coord in remove_list:
					line.remove(remove_coord)
		return untested_cells
					

	def kn_ki_possibilities_moves(self,src_coord):
		untested_cells = self.return_figure(src_coord).untested_possible_moves(src_coord)
		# if not untested_cells[0]:
			# pass
		# else:
		remove_list = []
		for dest_coord in untested_cells[0]:
			if self.return_figure(dest_coord) != 'empty' and self.return_colour_figure(dest_coord) == self.return_colour_figure(src_coord):
				remove_list.append(dest_coord)
		for remove_coord in remove_list:
			untested_cells[0].remove(remove_coord)
		return untested_cells

	
	def give_figure_color(self,coord):

		''' опр цвет'''
		pass


	def game_is_ready(self):
		pass


	def checkup_for_check(self, attack_col, defense_col):
		pass


	def checkup_empty_space(self, scr_coord):
		'''Проверяет поле находится ли на нём фигура
		'''
		num, let = self.uncover_values(scr_coord)
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

	def return_figure(self, coord):
		num, let = self.uncover_values(coord)
		return self.board[num][let]['figure']


	def return_colour_figure(self, coord):
		num, let = self.uncover_values(coord)
		return self.board[num][let]['figure'].colour


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

		# TEST
		self.board['5']['h']['figure'] = King('White')
		self.board['6']['h']['figure'] = Knight('White')


		# TEST

		# # black

		# TEST
		self.board['4']['h']['figure'] = Pawn('Black', False)
		self.board['4']['g']['figure'] = Pawn('Black', False)
		# TEST

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


	def move_from_to(self, src_coord, dest_coord):
		'''
		move figure
		''' 
		src_num, src_let =self.uncover_values(src_coord)
		dest_num, dest_let = self.uncover_values(dest_coord)
		if self.board[src_num][src_let]['figure'].untouched: 
			self.board[src_num][src_let]['figure'].touch()
		self.board[dest_num][dest_let]['figure'] = self.board[src_num][src_let]['figure']
		self.board[src_num][src_let]['figure'] = 'empty'

	
	def uncover_values(self,*args,**kwargs):
		'''invert arguments
		(('1','a')) -> ('1','a')
		(('a','1')) -> ('1','a')
		['1','a'] -> ('1','a')
		['a','1'] -> ('1','a')
		('1','a') -> ('1','a')
		('a','1') -> ('1','a')
		{'num':'1' ,'let':'a'} -> ('1','a')
		{'let':'a', 'num':'1'} -> ('1','a')
		'''
		if len(kwargs) == 2:
			return kwargs['num'], kwargs['let']
		if len(args) == 1:
			if isinstance(args[0], (list, tuple)):
				if (args[0][0].isdigit()):
					return (args[0][0], args[0][1])
				elif (args[0][1].isdigit()):
					return (args[0][1], args[0][0])
		elif len(args) == 2:
			if args[0].isdigit():
				return args[0],args[1]
			elif args[1].isdigit():
				return args[1],args[0]
		raise ValueError("Not right arguments for function 'uncover_values(self,*args,**kwargs)'")	

a = Chessboard()
a.filling()
a.print()

print('\n'*2)
print(a.kn_ki_possibilities_moves( ('5','h') ))
# print(a.rbq_possibilities_moves( ('1','d')))

# while True:
# 	input()
# 	print()
# 	l = input('Введите откуда столбец:')
# 	n = input('Введите откуда строку:')
# 	l1 = input('Введите куда столбец:')
# 	n1 = input('Введите куда строка:')
# 	a.move_from_to([n,l],[n1,l1])
# 	print('\n'*2)
# 	a.print()

	# print(id(a.board['1']['a']))
	# print(id(a.board['1']['b']))



