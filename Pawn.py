from Func import to_index, to_position
from ChessPiece import ChessPiece


class Pawn(ChessPiece):

    def __str__(self):
        return f"♙"

    def checkMoves(self):
        self.availableMoves = []
        row, column = to_index(self.position)
        try:
            if self.color == "White" and int(self.position[1]) == 2 and self.board.positions[row - 2][column] == 0 and \
                    self.board.positions[row - 1][column] == 0:
                self.availableMoves.append([row - 2, column])
        except:
            pass
        try:
            if self.color == "Black" and int(self.position[1]) == 7 and self.board.positions[row + 2][column] == 0 and \
                    self.board.positions[row + 1][column] == 0:
                self.availableMoves.append([row + 2, column])
        except:
            pass
        try:
            if self.color == "White" and self.board.positions[row - 1][column] == 0:
                self.availableMoves.append([row - 1, column])
        except:
            pass
        try:
            if self.color == "White" and self.board.positions[row - 1][column + 1].color == "Black":
                self.availableMoves.append([row - 1, column + 1])
        except:
            pass
        try:
            if self.color == "White":
                if not [row - 1, column + 1] in self.board.whiteHits[Pawn]:
                    self.board.whiteHits[Pawn].append([row - 1,column + 1])
        except:
            pass
        try:
            if column!=0 and self.color == "White" and self.board.positions[row - 1][column - 1].color == "Black":
                self.availableMoves.append([row - 1, column - 1])
        except:
            pass
        try:
            if column!=0 and self.color == "White":
                if not [row - 1, column - 1] in self.board.whiteHits[Pawn]:
                    self.board.whiteHits[Pawn].append([row - 1,column - 1])
        except:
            pass
        try:
            if self.color == "Black" and self.board.positions[row + 1][column] == 0:
                self.availableMoves.append([row + 1, column])
        except:
            pass
        try:
            if self.board.positions[row + 1][column + 1] != 0 and self.color == "Black" and \
                    self.board.positions[row + 1][column + 1].color == "White":
                self.availableMoves.append([row + 1, column + 1])
        except:
            pass
        try:
            if self.color == "Black":
                if not [row + 1, column + 1] in self.board.blackHits[Pawn]:
                    self.board.blackHits[Pawn].append([row + 1,column + 1])
        except:
            pass
        try:
            if column!=0 and self.board.positions[row + 1][column - 1] != 0 and self.color == "Black" and \
                    self.board.positions[row + 1][column - 1].color == "White":
                self.availableMoves.append([row + 1, column - 1])
        except:
            pass
        try:
            print(self.board.positions[row + 1][column - 1])
            if column!=0 and self.color == "Black":
                if not [row + 1, column - 1] in self.board.blackHits[Pawn]:
                    self.board.blackHits[Pawn].append([row + 1,column - 1])
        except:
            pass

