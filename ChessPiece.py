from Func import to_index, to_position

class ChessPiece:
    def __init__(self, color, position, board):
        self.color = color
        self.position = position
        self.availableMoves = []
        self.board = board

    def movePiece(self, move):
        self.checkMoves()
        print(self.availableMoves, to_index(move))
        if list(to_index(move)) in self.availableMoves:
            moveIndex = to_index(move)
            if self.board.positions[moveIndex[0]][moveIndex[1]] != 0:
                slef.board.eated.append(self.board.positions[moveIndex[0]][moveIndex[1]])
            self.board.positions[moveIndex[0]][moveIndex[1]] = self
            self.board.positions[to_index(self.position)[0]][to_index(self.position)[1]] = 0
            self.position = move
            if self.board.moveTime == "White":
                self.board.moveTime = "Black"
            else:
                self.board.moveTime = "White"
        else:
            print("Move not available")
            print(f"The available moves are: {[to_position(i) for i in self.availableMoves]}")

    def checkMoves(self):
        pass

    def updatePosition(self, move):
        self.position = move


