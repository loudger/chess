

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
    def __init__(self, color):
        self.color = color
        self.untouched = True

    def touch(self):
        self.untouched = False

    def __repr__(self):
        return repr(self.__class__.__name__)


class King(Figure):
    
    pass


class Queen(Figure):
    pass


class Bishop(Figure):
    pass


class Knight(Figure):
    pass


class Rook(Figure):
    pass


class Pawn(Figure):
    pass


