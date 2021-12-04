measurements = []
def sum_measurements(measurements, steps):
    increased_count = 0
    for i in range (0, len(measurements) - steps):
        if sum(measurements[i+1:i+steps+1]) > sum(measurements[i:i+steps]):
            increased_count += 1
    return increased_count
print(sum_measurements(measurements, 3))