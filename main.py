from Board import Board
from Func import to_position


if __name__ == "__main__":

    board = Board()

    board.print_board()
    while (1):
        piece = input(f"Turn of {board.moveTime}\nSelect piece: ")
        move = input("Place to Move: ")

        board.make_move(piece, move)
        board.print_board()
        for a in board.whiteHits.keys():
            print(f"\nWhite {a.__name__} hits:")
            for b in board.whiteHits[a]:
                print(f"{to_position(b)}", end=", ")
        for a in board.blackHits.keys():
            print(f"\nBlack {a.__name__} hits:")
            for b in board.blackHits[a]:
                print(f"{to_position(b)}", end=", ")

