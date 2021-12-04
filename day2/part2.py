
def serialize_input_commands():
    input_file = open('day2/input.txt', 'r')
    lines = input_file.readlines()
    commands = []
    for line in lines:
        command = line.split()
        commands.append({"direction": command[0], "position": int(command[1])})

    return commands

def calculate_position(commands):
    horizontal_pos = 0
    depth = 0
    aim = 0

    for command in commands:
        if command["direction"] == "forward":
            horizontal_pos += command["position"]
            depth += (aim * command["position"])
        elif command["direction"] == "down":
            aim += command["position"]
        elif command["direction"] == "up":
            aim -= command["position"]
        else:
            continue

    return horizontal_pos * depth

def main():
    print("{}".format(calculate_position(serialize_input_commands())))

if __name__ == "__main__":
    main()
