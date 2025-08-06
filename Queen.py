from Func import to_index, to_position
from ChessPiece import ChessPiece


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
                    if self.color == "White":
                        self.board.whiteHits[Queen].append(self.board.positions[row + i][column + i])
                    else:
                        self.board.blackHits[Queen].append(self.board.positions[row + i][column + i])
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
                    if self.color == "White":
                        self.board.whiteHits[Queen].append(self.board.positions[row - i][column - i])
                    else:
                        self.board.blackHits[Queen].append(self.board.positions[row - i][column - i])
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
                    if self.color == "White":
                        self.board.whiteHits[Queen].append(self.board.positions[row - i][column + i])
                    else:
                        self.board.blackHits[Queen].append(self.board.positions[row - i][column + i])
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
                    if self.color == "White":
                        self.board.whiteHits[Queen].append(self.board.positions[row + i][column - i])
                    else:
                        self.board.blackHits[Queen].append(self.board.positions[row + i][column - i])
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
                    if self.color == "White":
                        self.board.whiteHits[Queen].append(self.board.positions[row + i][column])
                    else:
                        self.board.blackHits[Queen].append(self.board.positions[row + i][column])   
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
                    if self.color == "White":
                        self.board.whiteHits[Queen].append(self.board.positions[row - i][column])
                    else:
                        self.board.blackHits[Queen].append(self.board.positions[row - i][column])   
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
                    if self.color == "White":
                        self.board.whiteHits[Queen].append(self.board.positions[row][column + i])
                    else:
                        self.board.blackHits[Queen].append(self.board.positions[row][column + i])   
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
                    if self.color == "White":
                        self.board.whiteHits[Queen].append(self.board.positions[row][column - i])
                    else:
                        self.board.blackHits[Queen].append(self.board.positions[row][column - i])
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

