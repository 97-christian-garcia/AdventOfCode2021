import copy

def serialize_binary():
    with open('day3/input.txt') as file:
        input = file.read().splitlines()
        lines = []
        for line in input:
            lines.append(line)
    return lines

def filter_list(input, pos, gas):
    bit_0_list = list(filter(lambda b: b[pos] == "0", input))
    bit_1_list = list(filter(lambda b: b[pos] == "1", input))

    if gas == "oxygen":
        return bit_0_list if len(bit_0_list) > len(bit_1_list) else bit_1_list # Most common value (1 for tiebreaker)
    else:
        return bit_0_list if len(bit_0_list) <= len(bit_1_list) else bit_1_list # Least common value (0 for tiebreaker)
    
def calculate_life_support(input):
    oxygen_list = input
    co2_list = copy.deepcopy(input)

    input_bits_length = len(input[0])
    pos_counter = 0
    while len(oxygen_list) > 1 and pos_counter < input_bits_length:
        oxygen_list = filter_list(oxygen_list, pos_counter, "oxygen")
        pos_counter += 1

    pos_counter = 0
    while len(co2_list) > 1 and pos_counter < input_bits_length:
        co2_list = filter_list(co2_list, pos_counter, "co2")
        pos_counter += 1
    
    # There should be only one element left once both lists are filtered
    return int(oxygen_list[0], 2) * int(co2_list[0], 2)

def main():
    print("{}".format(calculate_life_support(serialize_binary())))

if __name__ == "__main__":
    main()
