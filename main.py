from Board import Board



if __name__ == "__main__":

    board = Board()

    board.print_board()
    while (1):
        piece = input(f"Turn of {board.moveTime}\nSelect piece: ")
        move = input("Place to Move: ")

        board.make_move(piece, move)
        board.print_board()
        print(board.whiteHits)
        print(board.blackHits)

