
def serialize_bingo():
    with open('day4/input.txt') as file:
        input = file.read().splitlines()
        calls = input[0].split(",")
        boards = [[]]
        input = input[2:] # Ignore call sequence and first newline
        current_board = 0
        for line in input:
            if not line: # Newline means new board
                current_board += 1
                boards.append([])
                continue
            boards[current_board].append([{"marked": False, "value": x} for x in line.split()])

    return calls, boards

def is_winner(row, column):
    unmarked_row_vals = list(filter(lambda r: r["marked"] == False, row))
    unmarked_column_vals = list(filter(lambda c: c["marked"] == False, column))

    if not unmarked_row_vals or not unmarked_column_vals:
        return True
    return False

def get_column(board, column_index):
    col = []
    for row in board:
        col.append(row[column_index])
    return col

def play_bingo(calls, boards):
    # NEEEEESSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTEEEEEEEEEEEEDDDDDDDDDDDDDDD
    # LOOOOOOOOOOOOOOOOOOOOOOOOPPPPPPPSSSSSSSSSSSSSSSSSS
    for call in calls:
        for board in boards:
            for row in board:
                column_index = 0
                for column in row:
                    if column["value"] == call:
                        column["marked"] = True
                        if is_winner(row, get_column(board, column_index)):
                            return call, board
                    column_index += 1

def main():
    calls, boards = serialize_bingo()
    winning_call, winning_board = play_bingo(calls, boards)
    unmarked_values = 0
    for row in winning_board:
        unmarked_values = unmarked_values + sum(int(r['value']) for r in row if not r['marked'])
    print("{}".format(int(winning_call) * unmarked_values))

if __name__ == "__main__":
    main()