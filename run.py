Desk = list[list[int]]

dimention_x, dimention_y = 7, 6
players_cnt = 2
winning_length = 4

desk = [
    [0 for y in range(dimention_x)]
    for y in range(dimention_y)
]

player_signs = [
    'x',
    'y',
    'z',
    *[chr(char_number) for char_number in range(ord('a'), ord('x'))],
]


def draw_desk(desk: Desk) -> str:
    # Draw column number
    column_numbers = [str(number) for number in range(1, dimention_x+1)]
    image = '|'.join(column_numbers) + '\n'

    # Draw separator
    image += '+'.join(['-'] * dimention_x) + '\n'

    # Draw rows one be one
    for row in desk:
        image += '|'.join([draw_cell(cell) for cell in row]) + '\n'

    return image


def draw_cell(cell: int) -> int:
    if cell:
        return player_signs[cell - 1]
    else:
        return ' '


def get_winner_number(desk: Desk) -> int:
    # Check rows
    for row in desk:
        for col in range(dimention_x - winning_length + 1):
            if all(
                row[col]
                and row[col] == row[col + offset]
                for offset in range(winning_length)
            ):
                return row[col]

    # Check columns
    for col in range(dimention_x):
        for row in range(dimention_y - winning_length + 1):
            if all(
                desk[row][col]
                and desk[row][col] == desk[row + offset][col]
                for offset in range(winning_length)
            ):
                return desk[row][col]

    # Check diagonals
    for row in range(dimention_y - winning_length + 1):
        for col in range(dimention_x - winning_length + 1):
            if all(
                desk[row][col]
                and desk[row][col] == desk[row + offset][col + offset]
                for offset in range(winning_length)
            ):
                return desk[row][col]

    for row in range(winning_length - 1, dimention_y):
        for col in range(dimention_x - winning_length + 1):
            if all(
                desk[row][col]
                and desk[row][col] == desk[row - offset][col + offset]
                for offset in range(winning_length)
            ):
                return desk[row][col]

    return 0  # No winner found


if __name__ == "__main__":
    game_finished = False
    while not game_finished:
        for player_number in range(1, players_cnt+1):
            player_sign = player_signs[player_number - 1]

            # Draw the desk
            print(draw_desk(desk))

            # Get player's input and place the ball
            while True:
                print(
                    f'Player {player_number} ({player_sign}) '
                    f'input the column number to place a ball:',
                    end='',
                )

                try:
                    column_number = int(input())
                except ValueError:
                    print("Please input a valid number.")
                    continue

                # Find a free cell in a column and place a ball there
                found_place = False
                try:
                    for j in reversed(range(dimention_y)):
                        if not desk[j][column_number - 1]:
                            desk[j][column_number - 1] = player_number
                            found_place = True
                            break
                except IndexError:
                    print(f"The column #{column_number} doesn't exist.")
                    continue

                if found_place:
                    break

                print(
                    "No free space in the column, "
                    "please choose another one."
                )

            # Check for a winning situation
            if winner_number := get_winner_number(desk):
                winner_sign = player_signs[winner_number - 1]
                print(draw_desk(desk))
                print(f"Player {winner_number} ({winner_sign}) win!")
                game_finished = True
                break
