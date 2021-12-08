def serialize_lanternfish():
    with open('day6/input.txt') as file:
       return [int(x) for x in file.read().split(",")] 

def simulate_lanternfish(lanternfish, max_simulated_days):
    fishies = [0] * 9
    for fish in lanternfish:
        fishies[fish] += 1

    for day in range(1, max_simulated_days + 1):
        new_fish_count=fishies[0]
        for fish in range(0, len(fishies) - 1):
            fishies[fish] = fishies[fish + 1]
        fishies[6] += new_fish_count
        fishies[8] = new_fish_count

    return(sum(fishies))

def main():
    print("{}".format(simulate_lanternfish(serialize_lanternfish(), 256)))

if __name__ == "__main__":
    main()
