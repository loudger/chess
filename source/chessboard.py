from figure import King, Queen, Bishop, Knight, Rook, Pawn


class Chessboard:
	def __init__(self):
		self.tmp_color_value = 'dark'
		self.board = {}
		for i in range(8,0,-1):
			self.board[str(i)] = dict.fromkeys(['a','b','c','d','e','f','g','h'], {
				'figure':'empty',
				'space_color': None
				})
			for let in ['a','b','c','d','e','f','g','h']:
				if self.tmp_color_value == 'dark':
					self.tmp_color_value = 'ligth'
				else: 
					if self.tmp_color_value == 'ligth':
						self.tmp_color_value = 'dark'
				print(i, end = ' ')
				print(let)
				print(self.tmp_color_value)
				self.board[str(i)][let]['space_color'] = self.tmp_color_value
		del self.tmp_color_value

	# def auxiliary_func_set_color(self):
	# 	if self.tmp_color_value == 'dark':
	# 		self.tmp_color_value = 'ligth'
	# 		return 'ligth'
	# 	else: 
	# 		if self.tmp_color_value == 'ligth':
	# 			self.tmp_color_value = 'dark'
	# 		return 'dark'

	def return_figure(self, num, let):
		return self.board[num][let]['figure']

	def return_color_space(self, num, let):
		return self.board[num][let]['color']

	def print(self):
		for i in range (8, -1, -1):
			print (str('-+{}-').format( (('-'*8)+'-+')*8) )
			if i != 0:
				print (i, end = '|')
				for let in ['a','b','c','d','e','f','g','h']:
					print (str('{}{}').format(self.board[str(i)][let]['figure'], 
						(lambda x: x.color[0:1] if x != 'empty' else '')(self.board[str(i)][let]['figure']) ) ,
					end =str(' '*(9-len(self.board[str(i)][let]['figure'].__str__()) - (lambda x: 0 if x == 'empty' else 1 )(self.board[str(i)][let]['figure']))+'|') )
				print()
		print(end = ' |')
		for let in ['a','b','c','d','e','f','g','h']:
			print ( str('    {}    ').format(let) ,end = '|')

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
		# black
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
		
		def checkup_for_check(self, attack_col, defense_col):
			pass

		def checkup_empty_space(self, num, let):
			if self.board[num][let] == 'empty':
				return True
			else:
				return False

		def checkup_space_for_move(self, num, let, own_col):
			if self.board[num][let] == 'empty':
				return True
			else:
				if self.board[num][let].color == own_col:
					return False
				else:
					return True


a = Chessboard()
a.filling()
# a.print()
print(a.board)
