# @author: Ezedin Fedlu
# @date: 2022-12-17
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 17


import sys


def parse_input(file_path):
    with open(file_path) as f:
        return f.read().strip()


def get_piece(piece_type, y_position):
    coordinates = set()
    if piece_type == 0:
        coordinates.update([(2, y_position), (3, y_position),
                           (4, y_position), (5, y_position)])
    elif piece_type == 1:
        coordinates.update([(3, y_position+2), (2, y_position+1),
                           (3, y_position+1), (4, y_position+1), (3, y_position)])
    elif piece_type == 2:
        coordinates.update([(2, y_position), (3, y_position),
                           (4, y_position), (4, y_position+1), (4, y_position+2)])
    elif piece_type == 3:
        coordinates.update([(2, y_position), (2, y_position+1),
                           (2, y_position+2), (2, y_position+3)])
    elif piece_type == 4:
        coordinates.update([(2, y_position+1), (2, y_position),
                           (3, y_position+1), (3, y_position)])
    else:
        assert False, "Invalid piece type"
    return coordinates


def move_left(piece):
    if any([x == 0 for (x, y) in piece]):
        return piece
    return set([(x-1, y) for (x, y) in piece])


def move_right(piece):
    if any([x == 6 for (x, y) in piece]):
        return piece
    return set([(x+1, y) for (x, y) in piece])


def move_down(piece):
    return set([(x, y-1) for (x, y) in piece])


def move_up(piece):
    return set([(x, y+1) for (x, y) in piece])


def show(board):
    max_y = max([y for (x, y) in board])
    for y in range(max_y, 0, -1):
        row = ''
        for x in range(7):
            if (x, y) in board:
                row += '#'
            else:
                row += ' '
        print(row)


def signature(board):
    max_y = max([y for (x, y) in board])
    return frozenset([(x, max_y-y) for (x, y) in board if max_y - y <= 30])


def simulate(data, max_turns):
    board = set([(x, 0) for x in range(7)]
                )  # Initialize the board with a solid row at the top
    cursor = 0
    turn = 0
    seen_states = {}
    top = 0
    added_height = 0
    while turn < max_turns:
        piece_type = turn % 5
        piece = get_piece(piece_type, top + 4)
        while True:
            if data[cursor] == '<':
                piece = move_left(piece)
                if piece & board:  # If the piece collides with the board, move it back to the right
                    piece = move_right(piece)
            else:
                piece = move_right(piece)
                if piece & board:  # If the piece collides with the board, move it back to the left
                    piece = move_left(piece)
            cursor = (cursor + 1) % len(data)
            piece = move_down(piece)
            if piece & board:
                piece = move_up(piece)
                board |= piece
                top = max([y for (x, y) in board])
                # Check if this board state has been seen before
                board_signature = (cursor, piece_type, signature(board))
                if board_signature in seen_states and turn >= 2022:
                    # If the board state has been seen before, calculate how many turns and how much height will be added
                    # until the next occurrence of this board state, and add that to the current turn and height
                    (old_turn, old_height) = seen_states[board_signature]
                    dy = top - old_height
                    dt = turn - old_turn
                    added_amount = (max_turns - turn) // dt
                    added_height += added_amount * dy
                    turn += added_amount * dt
                    assert turn <= max_turns
                seen_states[board_signature] = (turn, top)
                break
        turn += 1
    return top + added_height


def main():
    data = parse_input(sys.argv[1])
    print(f"Part 1: {simulate(data, 2022)}")
    print(f"Part 2: {simulate(data, 1000000000000)}")


if __name__ == "__main__":
    main()
