def serialize_binary():
    with open('day3/input.txt') as file:
        input = file.read().splitlines()
        lines = []
        for line in input:
            lines.append(line)
    return lines

def calculate_power_consumption(input):
    input_bits_length = (len(input[0]))
    bit_0_count = [0] * input_bits_length
    bit_1_count = [0] * input_bits_length

    for i in range(0, len(input)):
        for b in range(0, input_bits_length):
            if input[i][b] == "0":
                bit_0_count[b] += 1
            elif input[i][b] == "1":
                bit_1_count[b] += 1
            else:
                continue

    print(bit_0_count)
    print(bit_1_count)

    gamma_rate_string = "" # Most common bit
    epsilon_rate_string = "" # Least common bit
    for i in range(0, input_bits_length):
        if bit_0_count[i] > bit_1_count[i]:
            print("0 occurs more at position {}".format(i))
            gamma_rate_string = gamma_rate_string + "0"
            epsilon_rate_string = epsilon_rate_string + "1"
        else:
            print("1 occurs more at position {}".format(i))
            gamma_rate_string = gamma_rate_string + "1"
            epsilon_rate_string = epsilon_rate_string + "0"

    print("gamma string: {} | decimal: {}".format(gamma_rate_string, int(gamma_rate_string, 2)))
    print("epsilon string: {} | decimal: {}".format(epsilon_rate_string, int(epsilon_rate_string, 2)))

    return int(gamma_rate_string, 2) * int(epsilon_rate_string, 2)

def main():
    print("{}".format(calculate_power_consumption(serialize_binary())))

if __name__ == "__main__":
    main()
