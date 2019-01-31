

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

    def __repr__(self):
        return repr(self.__class__.__name__)


class King(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)
        self.untouched = True


class Queen(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)


class Bishop(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)


class Knight(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)


class Rook(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)
        self.untouched = True


class Pawn(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)
        self.untouched = True


