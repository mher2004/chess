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
            if row + checkMove[0] > 7 or row + checkMove[0] < 1 or column + checkMove[1] > 7 or column + checkMove[
                1] < 1:
                continue
            
            if self.board.positions[row + checkMove[0]][column + checkMove[1]] == 0:
                if self.color == "White":
                    for key in self.board.blackHits.keys():
                        if self.board.blackHits[key] == []:
                            continue
                        for hit in self.board.blackHits[key]:
                            if hit == [row + checkMove[0], column + checkMove[1]]:
                                self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
                else:
                    for key in self.board.whiteHits.keys():
                        if self.board.whiteHits[key] == []:
                            continue
                        for hit in self.board.whiteHits[key]:
                            if hit == [row + checkMove[0], column + checkMove[1]]:
                                self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
                
