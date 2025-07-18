def to_index(action):
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    if len(action) != 2:
        print("Wrong move!\n")
        return False
    elif not action[0] in letters:
        print("Wrong move!\n")
        return False
    elif int(action[1]) > 8 or int(action[1]) < 1:
        print("Wrong move!\n")
        return False
    column, row = letters.index(action[0]), 8-int(action[1])
    return row, column


class Board:
    def __init__(self):
        """
        K - stands for King,
        Q - stands for Queen,
        B - stands for Bishop(pix),
        H - stands for Horse,
        T - stands for Tower,
        P - stands for Pawn,
        """
        self.positions = [
            ["T", "H", "B", "Q", King("Black", "e8", self), "B", "H", "T"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0,   King("White", "e3", self), 0, 0, 0],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["T", "H", "B", "Q", King("White", "e1", self), "B", "H", "T"]
        ]
        self.eated = []
        self.moveTime = "White"

    def make_move(self, move):
        if to_index(move[:2]) == False or to_index(move[2:] == False):
            return False
        pieceRow, pieceColumn = to_index(move[:2])
        moveRow, moveColumn = to_index(move[2:])
        if self.positions[pieceRow][pieceColumn] == 0:
            print("Wrong move!\nThere is no piece in there.\n")
            return False
        elif self.positions[pieceRow][pieceColumn].color != self.moveTime:
            print(f"Wrong move!\nIt`s not your moving time, it`s {self.moveTime}`s moving time.\n")
            return False

    def print_board(self):
        k = 8
        for i in self.positions:
            print(k, " ", end="")
            for j in i:
                if j == 0:
                    a = " "
                else:
                    a = j
                print(f"|{a}", end="")
            print("|")
            k -= 1
        print("    A B C D E F G H")


class ChessPiece:
    def __init__(self, color, position, board):
        self.color = color
        self.position = position
        self.availableMoves = []
        self.board = board

    def checkMoves(self):
        pass

    def updatePosition(self, move):
        self.position = move


class King(ChessPiece):
    def checkMoves(self):
        row, column = to_index(self.position)
        checkMatrix = [
            [1, -1], [1, 0], [1, 1],
            [0, -1], [0, 0], [0, 1],
            [-1, -1], [-1, 0], [-1, 1],
        ]
        print(row,column)
        for checkMove in checkMatrix:
            if row + checkMove[0] > 7 or row + checkMove[0] < 1 or column + checkMove[1] > 7 or column + checkMove[
                1] < 1:
                continue
            if self.board.positions[row + checkMove[0]][column + checkMove[1]] == 0:
                self.availableMoves.append([row + checkMove[0], column + checkMove[1]])

aaaa = Board()

aaaa.positions[5][4].checkMoves()
print(aaaa.positions[5][4].availableMoves)