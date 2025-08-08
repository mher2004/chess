from Func import to_index, to_position
from King import King
from Queen import Queen
from Horse import Horse
from Pawn import Pawn
from Town import Town
from Bishop import Bishop

class Style:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RESET = "\033[0m"



class Board:
    def __init__(self):

        self.positions = [
            [Town("Black", "a8", self), Horse("Black", "b8", self), Bishop("Black", 'c8', self),
             Queen('Black', "d8", self),
             King("Black", "e8", self), Bishop('Black', "f8", self), Horse("Black", "g8", self),
             Town("Black", "h8", self)],
            [Pawn("Black", "a7", self), Pawn("Black", "b7", self), Pawn("Black", "c7", self), Pawn("Black", "d7", self),
             Pawn("Black", "e7", self), Pawn("Black", "f7", self), Pawn("Black", "g7", self),
             Pawn("Black", "h7", self)],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [Pawn("White", "a2", self), Pawn("White", "b2", self), Pawn("White", "c2", self), Pawn("White", "d2", self),
             Pawn("White", "e2", self), Pawn("White", "f2", self), Pawn("White", "g2", self),
             Pawn("White", "h2", self)],
            [Town("White", "a1", self), Horse("White", "b1", self), Bishop("White", "c1", self),
             Queen('White', "d1", self),
             King("White", "e1", self), Bishop('White', "f1", self), Horse("White", "g1", self),
             Town("White", "h1", self)]
        ]
        self.eated = []
        
        self.moveTime = "White"
        
        self.blackHits = {
            Pawn: [],
            Horse: [],
            Bishop: [],
            Town: [],
            Queen: [],
            King: []
        }
        self.whiteHits = {
            Pawn: [],
            Horse: [],
            Bishop: [],
            Town: [],
            Queen: [],
            King: []
        }

    def updateHits(self):
        self.blackHits = {
            Pawn: [],
            Horse: [],
            Bishop: [],
            Town: [],
            Queen: [],
            King: []
        }
        self.whiteHits = {
            Pawn: [],
            Horse: [],
            Bishop: [],
            Town: [],
            Queen: [],
            King: []
        }
        for a in self.positions:
            for b in a:
                if b != 0:
                    b.checkMoves()

    def make_move(self, piece, move):
        self.updateHits()
        if to_index(piece) == False or to_index(move) == False:
            return False
        pieceRow, pieceColumn = to_index(piece)
        moveRow, moveColumn = to_index(move)
        if self.positions[pieceRow][pieceColumn] == 0:
            print("Wrong move!\nThere is no piece in there.\n")
            return False
        elif self.positions[pieceRow][pieceColumn].color != self.moveTime:
            print(f"Wrong move!\nIt`s not your moving time, it`s {self.moveTime}`s moving time.\n")
            return False
        else:
            self.positions[pieceRow][pieceColumn].movePiece(move)
            self.updateHits()

    def print_board(self):
        k = 8
        for i in self.positions:
            print(k, " ", end="")
            for j in i:
                if j == 0:
                    a = "| "
                    print(a, end="")
                else:
                    a = j
                    if a.color == "Black":
                        print(f"|{Style.RED}{a}{Style.RESET}", end="")
                    else:
                        print(f"|{a}", end="")

            print("|")
            k -= 1
        print("    A B C D E F G H")



