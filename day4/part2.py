
def serialize_bingo():
    with open('day4/input.txt') as file:
        input = file.read().splitlines()
        bingo = {"calls": input[0].split(","), "boards": []}
        input = input[1:] # Ignore call sequence
        current_board = -1
        for line in input:
            if not line: # Newline means new board
                current_board += 1
                bingo["boards"].append({"winner": False, "values": []})
                continue
            
            bingo["boards"][current_board]["values"].append([{"marked": False, "value": x} for x in line.split()])

    return bingo

def is_winner(row, column):
    unmarked_row_vals = list(filter(lambda r: r["marked"] == False, row))
    unmarked_column_vals = list(filter(lambda c: c["marked"] == False, column))

    if not unmarked_row_vals or not unmarked_column_vals:
        return True
    return False

def get_column(board, column_index):
    col = []
    for row in board["values"]:
        col.append(row[column_index])
    return col

def play_bingo(calls, boards):
    winning_boards = 0

    # NEEEEESSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTEEEEEEEEEEEEDDDDDDDDDDDDDDD
    # LOOOOOOOOOOOOOOOOOOOOOOOOPPPPPPPSSSSSSSSSSSSSSSSSS
    for call in calls:
        for board in boards:
            if board["winner"]:
                continue
            for row in board["values"]:
                column_index = 0
                for column in row:
                    if column["value"] == call:
                        column["marked"] = True
                        if is_winner(row, get_column(board, column_index)):
                            board["winner"] = True
                            winning_boards += 1
                            if winning_boards == len(boards):
                                return {"call": call, "board": board["values"]}
                    column_index += 1

def main():
    game = serialize_bingo()
    winner = play_bingo(game["calls"], game["boards"])
    unmarked_values = 0
    for row in winner["board"]:
        unmarked_values = unmarked_values + sum(int(r['value']) for r in row if not r['marked'])
    print("{}".format(int(winner["call"]) * unmarked_values))

if __name__ == "__main__":
    main()