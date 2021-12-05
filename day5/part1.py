
def serialize_coords():
    with open('day5/input.txt') as file:
        input = file.read().splitlines()
        coords = []
        maxWidth = 0
        maxHeight = 0
        for line in input:
            startCoords, endCoords = line.split("->")
            startX, startY = startCoords.split(",")
            endX, endY = endCoords.split(",")

            startX = int(startX)
            startY = int(startY)
            endX = int(endX)
            endY = int(endY)

            if startX != endX and startY != endY:
                continue

            if startX > maxWidth:
                maxWidth = startX
            if startY > maxHeight:
                maxHeight = startY
            if endX > maxWidth:
                maxWidth = endX
            if endY > maxHeight:
                maxHeight = endY

            coords.append({"startX": startX, "startY": startY, "endX": endX, "endY": endY})

    grid = []
    for i in range(0, maxWidth + 1):
        grid.append([0] * (maxHeight + 1))

    return coords, grid

def map_vents(coords, grid):
    overlapped_points = 0
    for c in coords:
        # Horitontal path
        if c["startX"] != c["endX"]:
            # Swap variables if start is larger than the end:
            if c["startX"] > c["endX"]:
                temp = c["startX"]
                c["startX"] = c["endX"]
                c["endX"] = temp

            for i in range(c["startX"], c["endX"] + 1):
                grid[i][c["startY"]] += 1
                if grid[i][c["startY"]] == 2: # Overlapped point found
                    overlapped_points += 1

        # Vertical path
        else:
            if c["startY"] > c["endY"]:
                temp = c["startY"]
                c["startY"] = c["endY"]
                c["endY"] = temp

            for i in range(c["startY"], c["endY"] + 1):
                grid[c["startX"]][i] += 1
                if grid[c["startX"]][i] == 2:
                    overlapped_points += 1

    print(grid)
    return overlapped_points

def main():
    coords, grid = serialize_coords()
    overlapped_points = map_vents(coords, grid)
    print(overlapped_points)

if __name__ == "__main__":
    main()