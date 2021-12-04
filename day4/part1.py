
def serialize_bingo():
    with open('day4/input.txt') as file:
        input = file.read().splitlines()
        bingo = {"calls": input[0].split(","), "boards": []}
        input = input[1:] # Ignore call sequence
        current_board = -1
        for line in input:
            if not line: # Newline means new board
                current_board += 1
                bingo["boards"].append([])
                continue
            
            bingo["boards"][current_board].append([{"marked": False, "value": x} for x in line.split()])

    return bingo

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
                column_index = -1
                for column in row:
                    column_index += 1
                    if column["value"] == call:
                        column["marked"] = True
                        if is_winner(row, get_column(board, column_index)):
                            return {"call": call, "board": board}

def main():
    game = serialize_bingo()
    winner = play_bingo(game["calls"], game["boards"])
    unmarked_values = 0
    for row in winner["board"]:
        unmarked_values = unmarked_values + sum(int(r['value']) for r in row if not r['marked'])
    print("{}".format(int(winner["call"]) * unmarked_values))

if __name__ == "__main__":
    main()