import statistics

def serialize_crabrave():
    with open('day7/input.txt') as file:
       return [int(x) for x in file.read().split(",")] 

def calculate_crabrave_fuel(crabs):
    median = statistics.median(crabs)

    fuel_cost = 0
    for crab_pos in crabs:
        fuel_cost += abs(median - crab_pos)

    return int(fuel_cost)

def main():
    print("{}".format(calculate_crabrave_fuel(serialize_crabrave())))

if __name__ == "__main__":
    main()

