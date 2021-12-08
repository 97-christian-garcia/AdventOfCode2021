import statistics, math

def serialize_crabrave():
    with open('day7/input.txt') as file:
       return [int(x) for x in file.read().split(",")] 

def calculate_crabrave_fuel(crabs):
    mean = int(math.floor(statistics.mean(crabs)))

    fuel_cost = 0
    for crab_pos in crabs:
        for i in range(1, abs(mean - crab_pos) + 1):
            fuel_cost += i

    return fuel_cost

def main():
    print("{}".format(calculate_crabrave_fuel(serialize_crabrave())))

if __name__ == "__main__":
    main()

