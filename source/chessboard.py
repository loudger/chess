from figure import King, Queen, Bishop, Knight, Rook, Pawn


class Chessboard:
	def __init__(self):
		self.board = {}
		for i in range(8,0,-1):
			self.board[str(i)] = dict.fromkeys(['a','b','c','d','e','f','g','h'], 'empty')

	def print(self):
		for i in range (8, -1, -1):
			print (str('-+{}-').format( (('-'*8)+'-+')*8) )
			if i != 0:
				print (i, end = '|')
				for let in ['a','b','c','d','e','f','g','h']:
					print (str('{}{}').format(self.board[str(i)][let], 
						(lambda x: x.color[0:1] if x != 'empty' else '')(self.board[str(i)][let]) ) ,
					end =str(' '*(9-len(self.board[str(i)][let].__str__()) - (lambda x: 0 if x == 'empty' else 1 )(self.board[str(i)][let]))+'|') )
				print()
		print(end = ' |')
		for let in ['a','b','c','d','e','f','g','h']:
			print ( str('    {}    ').format(let) ,end = '|')

	def filling(self):
		# white
		for let in ['a', 'h']:
			self.board['1'][let] = Rook('White')
		for let in ['b', 'g']:
			self.board['1'][let] = Knight('White')
		for let in ['c', 'f']:
			self.board['1'][let] = Bishop('White')
		self.board['1']['e'] = King('White')
		self.board['1']['d'] = Queen('White')
		for let in ['a','b','c','d','e','f','g','h']:
			self.board['2'][let] = Pawn('White')
		# black
		for let in ['a', 'h']:
			self.board['8'][let] = Rook('Black')
		for let in ['b', 'g']:
			self.board['8'][let] = Knight('Black')
		for let in ['c', 'f']:
			self.board['8'][let] = Bishop('Black')
		self.board['8']['e'] = King('Black')
		self.board['8']['d'] = Queen('Black')
		for let in ['a','b','c','d','e','f','g','h']:
			self.board['7'][let] = Pawn('Black')
		
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
a.print()
