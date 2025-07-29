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
    column, row = letters.index(action[0]), 8 - int(action[1])
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
            [Pawn("Black", "a2", self), Pawn("Black", "b2", self), Pawn("Black", "c2", self), Pawn("Black", "d2", self),
             Pawn("Black", "e2", self), Pawn("Black", "f2", self), Pawn("Black", "g2", self),
             Pawn("Black", "h2", self)],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [Pawn("White", "a7", self), Pawn("White", "b7", self), Pawn("White", "c7", self), Pawn("White", "d7", self),
             Pawn("White", "e7", self), Pawn("White", "f7", self), Pawn("White", "g7", self),
             Pawn("White", "h7", self)],
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
    def __str__(self):
        return f"K"

    def checkMoves(self):
        row, column = to_index(self.position)
        checkMatrix = [
            [1, -1], [1, 0], [1, 1],
            [0, -1], [0, 1],
            [-1, -1], [-1, 0], [-1, 1],
        ]
        print(row, column)
        for checkMove in checkMatrix:
            if row + checkMove[0] > 7 or row + checkMove[0] < 1 or column + checkMove[1] > 7 or column + checkMove[
                1] < 1:
                continue
            if self.board.positions[row + checkMove[0]][column + checkMove[1]] == 0:
                self.availableMoves.append([row + checkMove[0], column + checkMove[1]])


class Pawn(ChessPiece):
    def __str__(self):
        return f"P"

    def checkMoves(self):
        row, column = to_index(self.position)

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
                self.availableMoves.append([row - 1, column])
        except:
            pass
        try:
            if self.color == "Black" and self.board.positions[row + 1][column + 1].color == "White":
                self.availableMoves.append([row - 1, column + 1])
        except:
            pass
        try:
            if self.color == "Black" and self.board.positions[row + 1][column - 1].color == "White":
                self.availableMoves.append([row - 1, column - 1])
        except:
            pass


class Horse(ChessPiece):
    def __str__(self):
        return f"H"

    def checkMoves(self):
        row, column = to_index(self.position)
        checkMatrix = [
            [-1, -2], [-1, 2], [-2, -1],
            [-2, 1], [1, -2], [1, 2],
            [2, -1], [2, 1]
        ]
        print(row, column)
        for checkMove in checkMatrix:
            if row + checkMove[0] > 7 or row + checkMove[0] < 1 or column + checkMove[1] > 7 or column + checkMove[
                1] < 1:
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
        return f"T"

    def checkMoves(self):
        row, column = to_index(self.position)

        # Down
        print("Down")
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
        print(self.availableMoves)
        print("Up")
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
        print(self.availableMoves)
        print("Right")
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
        print(self.availableMoves)
        print("Left")
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


aaaa = Board()

aaaa.print_board()
aaaa.positions[3][1].checkMoves()
print(aaaa.positions[3][1].availableMoves)
