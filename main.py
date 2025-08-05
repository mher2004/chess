class Style:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RESET = "\033[0m"


def to_index(action):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if len(action) != 2:
        print("Wrong move!1\n")
        return False
    elif not action[0] in letters:
        print("Wrong move!2\n")
        return False
    elif int(action[1]) > 8 or int(action[1]) < 1:
        print("Wrong move!3\n")
        return False
    column, row = letters.index(action[0]), 8 - int(action[1])
    return row, column


def to_position(index):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    return letters[index[1]] + str(8 - index[0])


print(to_position(to_index("b1")))


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
        # for a in self.positions:
        #     for b in a:
        #         if b != 0:
        #             b.checkMoves()

    def make_move(self, piece, move):
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
                self.availableMoves.append([row + checkMove[0], column + checkMove[1]])


class Pawn(ChessPiece):

    def __str__(self):
        return f"♙"

    def checkMoves(self):
        self.availableMoves = []
        row, column = to_index(self.position)
        try:
            if self.color == "White" and int(self.position[1]) == 2 and self.board.positions[row - 2][column] == 0:
                self.availableMoves.append([row - 2, column])
        except:
            pass
        try:
            if self.color == "Black" and int(self.position[1]) == 7 and self.board.positions[row + 2][column] == 0:
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
            if self.color == "White" and self.board.positions[row - 1][column - 1].color == "Black":
                self.availableMoves.append([row - 1, column - 1])
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
            if self.board.positions[row + 1][column - 1] != 0 and self.color == "Black" and \
                    self.board.positions[row + 1][column - 1].color == "White":
                self.availableMoves.append([row + 1, column - 1])
        except:
            pass


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
                elif self.color == "White" and self.board.positions[row + checkMove[0]][
                    column + checkMove[1]].color == "Black":
                    self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
                elif self.color == "Black" and self.board.positions[row + checkMove[0]][
                    column + checkMove[1]].color == "White":
                    self.availableMoves.append([row + checkMove[0], column + checkMove[1]])
            except:
                continue


class Town(ChessPiece):
    def __str__(self):
        return f"♖"

    def checkMoves(self):
        self.availableMoves = []
        row, column = to_index(self.position)

        # Down
        for i in range(7):
            i += 1
            if row + i == 8:
                break
            try:
                if self.board.positions[row + i][column] == 0:
                    self.availableMoves.append([row + i, column])
                elif self.board.positions[row + i][column].color == "White" and self.color == "Black":
                    self.availableMoves.append([row + i, column])
                    break
                elif self.board.positions[row + i][column].color == "Black" and self.color == "White":
                    self.availableMoves.append([row + i, column])
                    break
                else:
                    break
            except:
                pass
        # Up
        for i in range(7):
            i += 1
            if row - i == -1:
                break
            try:
                if self.board.positions[row - i][column] == 0:
                    self.availableMoves.append([row - i, column])
                elif self.board.positions[row - i][column].color == "White" and self.color == "Black":
                    self.availableMoves.append([row - i, column])
                    break
                elif self.board.positions[row - i][column].color == "Black" and self.color == "White":
                    self.availableMoves.append([row - i, column])
                    break
                else:
                    break
            except:
                pass
        # Right
        for i in range(7):
            i += 1
            if column + i == 8:
                break
            try:
                if self.board.positions[row][column + i] == 0:
                    self.availableMoves.append([row, column + i])
                elif self.board.positions[row][column + i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row, column + i])
                    break
                elif self.board.positions[row][column + i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row, column + i])
                    break
                else:
                    break
            except:
                pass
        # Left
        for i in range(7):
            i += 1
            if column - i == -1:
                break
            try:
                if self.board.positions[row][column - i] == 0:
                    self.availableMoves.append([row, column - i])
                elif self.board.positions[row][column - i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row, column - i])
                    break
                elif self.board.positions[row][column - i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row, column - i])
                    break
                else:
                    break

            except:
                pass


class Bishop(ChessPiece):
    def __str__(self):
        return f"♗"

    def checkMoves(self):
        self.availableMoves = []
        row, column = to_index(self.position)

        # Down
        for i in range(7):
            i += 1
            if row + i == 8 or column + i == 8:
                break
            try:
                if self.board.positions[row + i][column + i] == 0:
                    self.availableMoves.append([row + i, column + i])
                elif self.board.positions[row + i][column].color == "White" and self.color == "Black":
                    self.availableMoves.append([row + i, column + i])
                    break
                elif self.board.positions[row + i][column + i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row + i, column + i])
                    break
                else:
                    break
            except:
                pass
        # Up
        for i in range(7):
            i += 1
            if row - i == -1 or column - i == -1:
                break
            try:
                if self.board.positions[row - i][column - i] == 0:
                    self.availableMoves.append([row - i, column - i])
                elif self.board.positions[row - i][column - i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row - i, column - i])
                    break
                elif self.board.positions[row - i][column - i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row - i, column - i])
                    break
                else:
                    break
            except:
                pass
        # Right
        for i in range(7):
            i += 1
            if column + i == 8 or row - i == -1:
                break
            try:
                if self.board.positions[row - i][column + i] == 0:
                    self.availableMoves.append([row - i, column + i])
                elif self.board.positions[row - i][column + i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row - i, column + i])
                    break
                elif self.board.positions[row - i][column + i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row - i, column + i])
                    break
                else:
                    break
            except:
                pass
        # Left
        for i in range(7):
            i += 1
            if column - i == -1 or row + i == 8:
                break
            try:
                if self.board.positions[row + i][column - i] == 0:
                    self.availableMoves.append([row + i, column - i])
                elif self.board.positions[row + i][column - i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row + i, column - i])
                    break
                elif self.board.positions[row + i][column - i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row + i, column - i])
                    break
                else:
                    break

            except:
                pass


class Queen(ChessPiece):
    def __str__(self):
        return f"♕"

    def checkMoves(self):
        self.availableMoves = []
        row, column = to_index(self.position)

        # Down
        for i in range(7):
            i += 1
            if row + i == 8 or column + i == 8:
                break
            try:
                if self.board.positions[row + i][column + i] == 0:
                    self.availableMoves.append([row + i, column + i])
                elif self.board.positions[row + i][column].color == "White" and self.color == "Black":
                    self.availableMoves.append([row + i, column + i])
                    break
                elif self.board.positions[row + i][column + i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row + i, column + i])
                    break
                else:
                    break
            except:
                pass
        # Up
        for i in range(7):
            i += 1
            if row - i == -1 or column - i == -1:
                break
            try:
                if self.board.positions[row - i][column - i] == 0:
                    self.availableMoves.append([row - i, column - i])
                elif self.board.positions[row - i][column - i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row - i, column - i])
                    break
                elif self.board.positions[row - i][column - i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row - i, column - i])
                    break
                else:
                    break
            except:
                pass
        # Right
        for i in range(7):
            i += 1
            if column + i == 8 or row - i == -1:
                break
            try:
                if self.board.positions[row - i][column + i] == 0:
                    self.availableMoves.append([row - i, column + i])
                elif self.board.positions[row - i][column + i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row - i, column + i])
                    break
                elif self.board.positions[row - i][column + i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row - i, column + i])
                    break
                else:
                    break
            except:
                pass
        # Left
        for i in range(7):
            i += 1
            if column - i == -1 or row + i == 8:
                break
            try:
                if self.board.positions[row + i][column - i] == 0:
                    self.availableMoves.append([row + i, column - i])
                elif self.board.positions[row + i][column - i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row + i, column - i])
                    break
                elif self.board.positions[row + i][column - i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row + i, column - i])
                    break
                else:
                    break

            except:
                pass
        # Down
        for i in range(7):
            i += 1
            if row + i == 8:
                break
            try:
                if self.board.positions[row + i][column] == 0:
                    self.availableMoves.append([row + i, column])
                elif self.board.positions[row + i][column].color == "White" and self.color == "Black":
                    self.availableMoves.append([row + i, column])
                    break
                elif self.board.positions[row + i][column].color == "Black" and self.color == "White":
                    self.availableMoves.append([row + i, column])
                    break
                else:
                    break
            except:
                pass
        # Up
        for i in range(7):
            i += 1
            if row - i == -1:
                break
            try:
                if self.board.positions[row - i][column] == 0:
                    self.availableMoves.append([row - i, column])
                elif self.board.positions[row - i][column].color == "White" and self.color == "Black":
                    self.availableMoves.append([row - i, column])
                    break
                elif self.board.positions[row - i][column].color == "Black" and self.color == "White":
                    self.availableMoves.append([row - i, column])
                    break
                else:
                    break
            except:
                pass
        # Right
        for i in range(7):
            i += 1
            if column + i == 8:
                break
            try:
                if self.board.positions[row][column + i] == 0:
                    self.availableMoves.append([row, column + i])
                elif self.board.positions[row][column + i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row, column + i])
                    break
                elif self.board.positions[row][column + i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row, column + i])
                    break
                else:
                    break
            except:
                pass
        # Left
        for i in range(7):
            i += 1
            if column - i == -1:
                break
            try:
                if self.board.positions[row][column - i] == 0:
                    self.availableMoves.append([row, column - i])
                elif self.board.positions[row][column - i].color == "White" and self.color == "Black":
                    self.availableMoves.append([row, column - i])
                    break
                elif self.board.positions[row][column - i].color == "Black" and self.color == "White":
                    self.availableMoves.append([row, column - i])
                    break
                else:
                    break

            except:
                pass


if __name__ == "__main__":

    board = Board()

    board.print_board()
    while (1):
        piece = input(f"Turn of {board.moveTime}\nSelect piece: ")
        move = input("Place to Move: ")

        board.make_move(piece, move)
        board.print_board()

