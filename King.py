from Func import to_index, to_position
from ChessPiece import ChessPiece

class King(ChessPiece):
    def __str__(self):
        return f"♔"

    def checkMoves(self):
        self.availableMoves = []
        row, column = to_index(self.position)
        checkMatrix = [
            [1, -1], [1, 0], [1, 1],
            [0, -1], [0, 1],
            [-1, -1], [-1, 0], [-1, 1],
        ]
        for checkMove in checkMatrix:
            if row + checkMove[0] > 7 or row + checkMove[0] < 0 or column + checkMove[1] > 7 or column + checkMove[
                1] < 0:
                continue
            
            if self.board.positions[row + checkMove[0]][column + checkMove[1]] == 0:
                if self.color == "White":
                    positionHitted = False
                    for key in self.board.blackHits.keys():
                        if [row + checkMove[0], column + checkMove[1]] in self.board.blackHits[key]:
                            positionHitted = True
                            break
                    if not positionHitted:
                        self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
                else:
                    positionHitted = False
                    for key in self.board.whiteHits.keys():
                        if [row + checkMove[0], column + checkMove[1]] in self.board.whiteHits[key]:
                            positionHitted = True
                            break
                    if not positionHitted:
                        self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
            elif self.board.positions[row + checkMove[0]][column + checkMove[1]].color != self.color:
                self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
            if self.color == "White":
                if not [row + checkMove[0], column + checkMove[1]] in self.board.whiteHits[King]:
                    self.board.whiteHits[King].append([row + checkMove[0], column + checkMove[1]])
            else:
                if not [row + checkMove[0], column + checkMove[1]] in self.board.blackHits[King]:
                    self.board.blackHits[King].append([row + checkMove[0], column + checkMove[1]])
                
