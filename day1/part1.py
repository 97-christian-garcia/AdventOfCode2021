measurements = []
increased_count = 0
for i in range (1, len(measurements) - 1):
    if measurements[i] > measurements[i - 1]:
        increased_count += 1
print(increased_count)