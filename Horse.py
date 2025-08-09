from Func import to_index, to_position
from ChessPiece import ChessPiece


class Horse(ChessPiece):
    def __str__(self):
        return f"♘"

    def checkMoves(self):
        self.availableMoves = []
        # print(self.position)
        row, column = to_index(self.position)
        checkMatrix = [
            [-1, -2], [-1, 2], [-2, -1],
            [-2, 1], [1, -2], [1, 2],
            [2, -1], [2, 1]
        ]
        for checkMove in checkMatrix:
            if row + checkMove[0] > 7 or row + checkMove[0] < 0 or column + checkMove[1] > 7 or column + checkMove[
                1] < 0:
                continue
            try:
                if self.board.positions[row + checkMove[0]][column + checkMove[1]] == 0:
                    self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
                    if self.color == "White":
                        self.board.whiteHits[Horse].append([row + checkMove[0], column + checkMove[1]])
                    else:
                        self.board.blackHits[Horse].append([row + checkMove[0], column + checkMove[1]])
                elif self.color == "White" and self.board.positions[row + checkMove[0]][
                    column + checkMove[1]].color == "Black":
                    self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
                elif self.color == "Black" and self.board.positions[row + checkMove[0]][
                    column + checkMove[1]].color == "White":
                    self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
                elif self.color == "White" and self.board.positions[row + checkMove[0]][
                    column + checkMove[1]].color == "White":
                    self.board.whiteHits[Horse].append([row + checkMove[0], column + checkMove[1]])
                elif self.color == "Black" and self.board.positions[row + checkMove[0]][
                    column + checkMove[1]].color == "Black":
                    self.board.blackHits[Horse].append([row + checkMove[0], column + checkMove[1]])
            except:
                continue

