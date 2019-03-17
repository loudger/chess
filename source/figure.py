

class Figure:
    
    """
    King - Король
    Queen - Ферзь
    Bishop - Слон
    Knight - Конь
    Rook - Ладья
    Pawn - Пешка

    untouced is True if the figure didn't move, else False
    give more possibility for King, Rook and Pawn
    """
    def __init__(self, colour, untouced = True):
        self.colour = colour
        self.untouched = untouced

    num_data = ['end','end','1','2','3','4','5','6','7','8','end','end']
    let_data = ['end','end','a','b','c','d','e','f','g','h','end','end']

    # hr - horizontally right
    # hl - horizontally left
    # vu - vertically up
    # vd - vertically left
    # dul - diagonally up left
    # dur - diagonally up right
    # ddl - diagonally down left
    # ddr - diagonally down right
    # _knight - special knight moves

    @staticmethod
    def _knight(coord):
        num, let = coord
        num_ind = Figure.num_data.index(num)
        let_ind = Figure.let_data.index(let)
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        result = []
        for cell in moves:
            tmp_coord = (Figure.num_data[num_ind+cell[0]], Figure.let_data[let_ind+cell[1]])
            if 'end' not in tmp_coord:
                result.append(tmp_coord)
        return result


    @staticmethod
    def hr(coord):
        '''returns the coordinate one cell to the right
        '''
        num, let = coord
        i = Figure.let_data.index(let)
        needed_let = Figure.let_data[i+1]
        if needed_let == 'end':
            return 'end'
        return (num, needed_let)

    @staticmethod
    def hl(coord):
        '''returns the coordinate one cell to the left
        '''
        num, let = coord
        i = Figure.let_data.index(let)
        needed_let = Figure.let_data[i-1]
        if needed_let == 'end':
            return 'end'
        return (num, needed_let)

    @staticmethod
    def vu(coord):
        '''returns the coordinate one cell to the up
        '''
        num, let = coord
        i = Figure.num_data.index(num)
        needed_num = Figure.num_data[i+1]
        if needed_num == 'end':
            return 'end'
        return (needed_num, let)

    @staticmethod
    def vd(coord):
        '''returns the coordinate one cell to the down
        '''
        num, let = coord
        i = Figure.num_data.index(num)
        needed_num = Figure.num_data[i-1]
        if needed_num == 'end':
            return 'end'
        return (needed_num, let)

    @staticmethod
    def dul(coord):
        '''returns the coordinate one cell to the up and left
        '''
        num, let = coord
        i = Figure.num_data.index(num)
        needed_num = Figure.num_data[i+1]
        if needed_num == 'end':
            return 'end'
        i = Figure.let_data.index(let)
        needed_let = Figure.let_data[i-1]
        if needed_let == 'end':
            return 'end'
        return (needed_num, needed_let)

    @staticmethod
    def dur(coord):
        '''returns the coordinate one cell to the up and right
        '''
        num, let = coord
        i = Figure.num_data.index(num)
        needed_num = Figure.num_data[i+1]
        if needed_num == 'end':
            return 'end'
        i = Figure.let_data.index(let)
        needed_let = Figure.let_data[i+1]
        if needed_let == 'end':
            return 'end'
        return (needed_num, needed_let)

    @staticmethod
    def ddl(coord):
        '''returns the coordinate one cell to the down and left
        '''
        num, let = coord
        i = Figure.num_data.index(num)
        needed_num = Figure.num_data[i-1]
        if needed_num == 'end':
            return 'end'
        i = Figure.let_data.index(let)
        needed_let = Figure.let_data[i-1]
        if needed_let == 'end':
            return 'end'
        return (needed_num, needed_let)

    @staticmethod
    def ddr(coord):
        '''returns the coordinate one cell to the down and right
        '''
        num, let = coord
        i = Figure.num_data.index(num)
        needed_num = Figure.num_data[i-1]
        if needed_num == 'end':
            return 'end'
        i = Figure.let_data.index(let)
        needed_let = Figure.let_data[i+1]
        if needed_let == 'end':
            return 'end'
        return (needed_num, needed_let)


    def touch(self):
        self.untouched = False

    def __repr__(self):
        return repr(self.__class__.__name__)





class King(Figure):
    
    def untested_possible_moves(self,src_coord):
        result = [[]]
        tmp_coord = Figure.vu(src_coord)
        if tmp_coord != 'end':
            result[0].append(tmp_coord)
        tmp_coord = Figure.dur(src_coord)
        if tmp_coord != 'end':
            result[0].append(tmp_coord)
        tmp_coord = Figure.hr(src_coord)
        if tmp_coord != 'end':
            result[0].append(tmp_coord)
        tmp_coord = Figure.ddr(src_coord)
        if tmp_coord != 'end':
            result[0].append(tmp_coord)
        tmp_coord = Figure.vd(src_coord)
        if tmp_coord != 'end':
            result[0].append(tmp_coord)
        tmp_coord = Figure.ddl(src_coord)
        if tmp_coord != 'end':
            result[0].append(tmp_coord)
        tmp_coord = Figure.hl(src_coord)
        if tmp_coord != 'end':
            result[0].append(tmp_coord)
        tmp_coord = Figure.dul(src_coord)
        if tmp_coord != 'end':
            result[0].append(tmp_coord)
        return result

class Queen(Figure):

    def untested_possible_moves(self,src_coord):
        result = [[],[],[],[],[],[],[],[]]
        tmp_coord = Figure.dur(src_coord)
        while tmp_coord != 'end':
            result[0].append(tmp_coord)
            tmp_coord = Figure.dur(tmp_coord)
        tmp_coord = Figure.ddr(src_coord)
        while tmp_coord != 'end':
            result[1].append(tmp_coord)
            tmp_coord = Figure.ddr(tmp_coord)
        tmp_coord = Figure.ddl(src_coord)
        while tmp_coord != 'end':
            result[2].append(tmp_coord)
            tmp_coord = Figure.ddl(tmp_coord)
        tmp_coord = Figure.dul(src_coord)
        while tmp_coord != 'end':
            result[3].append(tmp_coord)
            tmp_coord = Figure.dul(tmp_coord)
        tmp_coord = Figure.vu(src_coord)
        while tmp_coord != 'end':
            result[4].append(tmp_coord)
            tmp_coord = Figure.vu(tmp_coord)
        tmp_coord = Figure.hr(src_coord)
        while tmp_coord != 'end':
            result[5].append(tmp_coord)
            tmp_coord = Figure.hr(tmp_coord)
        tmp_coord = Figure.vd(src_coord)
        while tmp_coord != 'end':
            result[6].append(tmp_coord)
            tmp_coord = Figure.vd(tmp_coord)
        tmp_coord = Figure.hl(src_coord)
        while tmp_coord != 'end':
            result[7].append(tmp_coord)
            tmp_coord = Figure.hl(tmp_coord)
        return result


class Bishop(Figure):
    
    def untested_possible_moves(self,src_coord):
        result = [[],[],[],[]]
        tmp_coord = Figure.dur(src_coord)
        while tmp_coord != 'end':
            result[0].append(tmp_coord)
            tmp_coord = Figure.dur(tmp_coord)
        tmp_coord = Figure.ddr(src_coord)
        while tmp_coord != 'end':
            result[1].append(tmp_coord)
            tmp_coord = Figure.ddr(tmp_coord)
        tmp_coord = Figure.ddl(src_coord)
        while tmp_coord != 'end':
            result[2].append(tmp_coord)
            tmp_coord = Figure.ddl(tmp_coord)
        tmp_coord = Figure.dul(src_coord)
        while tmp_coord != 'end':
            result[3].append(tmp_coord)
            tmp_coord = Figure.dul(tmp_coord)
        print(result)
        return result


class Knight(Figure):
    
    def untested_possible_moves(self,src_coord):
        '''result = [[(),(),()]]
        '''
        result = [Figure._knight(src_coord)]
        return result

class Rook(Figure):
    
    def untested_possible_moves(self,src_coord):
        '''src = ('1','a')
        '''
        result = [[],[],[],[]]
        tmp_coord = Figure.vu(src_coord)
        while tmp_coord != 'end':
            result[0].append(tmp_coord)
            tmp_coord = Figure.vu(tmp_coord)
        tmp_coord = Figure.hr(src_coord)
        while tmp_coord != 'end':
            result[1].append(tmp_coord)
            tmp_coord = Figure.hr(tmp_coord)
        tmp_coord = Figure.vd(src_coord)
        while tmp_coord != 'end':
            result[2].append(tmp_coord)
            tmp_coord = Figure.vd(tmp_coord)
        tmp_coord = Figure.hl(src_coord)
        while tmp_coord != 'end':
            result[3].append(tmp_coord)
            tmp_coord = Figure.hl(tmp_coord)
        return result
        
            



class Pawn(Figure):
    
    def untested_possible_moves(self,src_coord):
        '''src_coord = ('1','a')
        '''
        result = [[],[]]
        if self.colour == 'White':
            tmp_coord = Figure.vu(src_coord)
            if tmp_coord != 'end':
                result[0].append(tmp_coord)
                if self.untouched == True:
                    tmp_coord = Figure.vu(tmp_coord)
                    if tmp_coord != 'end':
                        result[0].append(tmp_coord)
            tmp_coord = Figure.dur(src_coord)
            if tmp_coord != 'end':
                result[1].append(tmp_coord)
            tmp_coord = Figure.dul(src_coord)
            if tmp_coord != 'end':
                result[1].append(tmp_coord)
        elif self.colour == 'Black':
            tmp_coord = Figure.vd(src_coord)
            if tmp_coord != 'end':
                result[0].append(tmp_coord)
                if self.untouched == True:
                    tmp_coord = Figure.vd(tmp_coord)
                    if tmp_coord != 'end':
                        result[0].append(tmp_coord)
            tmp_coord = Figure.ddr(src_coord)
            if tmp_coord != 'end':
                result[1].append(tmp_coord)
            tmp_coord = Figure.ddl(src_coord)
            if tmp_coord != 'end':
                result[1].append(tmp_coord)
        return result

# pa = Rook('Black')


# print(pa.untested_possible_moves(('2','b')))