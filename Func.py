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

