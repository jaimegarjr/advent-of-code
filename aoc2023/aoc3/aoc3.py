gearMap = {}


def build2DArray(lines):
    grid = []
    for l in lines:
        row = []
        for c in l:
            row.append(c)
        grid.append(row)

    return grid


def findAdjacentNumber(grid, r, c):
    ROW_MAX, COL_MAX = len(grid), len(grid[0])
    numEnd = c
    for i in range(c, COL_MAX):
        if grid[r][i].isdigit():
            continue
        else:
            numEnd = i
            break

    if numEnd == c:
        numEnd = COL_MAX

    return grid[r][c:numEnd], len(grid[r][c:numEnd])


def checkAllAdjacent(grid, r, c, numArr, length):
    ROW_MAX, COL_MAX = len(grid), len(grid[0])
    res = []
    # check all elements around element gric[r][c] with number length

    # loop through left column surrounding element
    for i in range(r - 1, r + 2):
        if (
            i >= 0
            and i < ROW_MAX
            and c - 1 >= 0
            and not grid[i][c - 1].isalnum()
            and not grid[i][c - 1] == "."
        ):
            if grid[i][c - 1] == "*":
                # add number to gear map with reference to * element
                if (i, c - 1) in gearMap:
                    gearMap[(i, c - 1)].append(int("".join(numArr)))
                else:
                    gearMap[(i, c - 1)] = [int("".join(numArr))]
            res.append(True)
        else:
            res.append(False)

    # loop through right column surrounding element
    for i in range(r - 1, r + 2):
        if (
            i >= 0
            and i < ROW_MAX
            and c + length < COL_MAX
            and not grid[i][c + length].isalnum()
            and not grid[i][c + length] == "."
        ):
            if grid[i][c + length] == "*":
                # add number to gear map with reference to * element
                if (i, c + length) in gearMap:
                    gearMap[(i, c + length)].append(int("".join(numArr)))
                else:
                    gearMap[(i, c + length)] = [int("".join(numArr))]
            res.append(True)
        else:
            res.append(False)

    # loop through top row surrounding element
    for i in range(c - 1, c + length + 1):
        if (
            i >= 0
            and i < COL_MAX
            and r - 1 >= 0
            and not grid[r - 1][i].isalnum()
            and not grid[r - 1][i] == "."
        ):
            if grid[r - 1][i] == "*":
                # add number to gear map with reference to * element
                if (r - 1, i) in gearMap:
                    gearMap[(r - 1, i)].append(int("".join(numArr)))
                else:
                    gearMap[(r - 1, i)] = [int("".join(numArr))]
            res.append(True)
        else:
            res.append(False)

    # loop through bottom row surrounding element
    for i in range(c - 1, c + length + 1):
        if (
            i >= 0
            and i < COL_MAX
            and r + 1 < ROW_MAX
            and not grid[r + 1][i].isalnum()
            and not grid[r + 1][i] == "."
        ):
            if grid[r + 1][i] == "*":
                # add number to gear map with reference to * element
                if (r + 1, i) in gearMap:
                    gearMap[(r + 1, i)].append(int("".join(numArr)))
                else:
                    gearMap[(r + 1, i)] = [int("".join(numArr))]
            res.append(True)
        else:
            res.append(False)

    if True in res:
        return True


def removeDups(gearMap):
    for k, v in gearMap.items():
        u_v = set(v)
        if len(u_v) > 1:
            gearMap[k] = list(u_v)
        else:
            gearMap[k] = []

    newGearMap = {k: v for k, v in gearMap.items() if v}
    return newGearMap


def parseMap(gearMap):
    products = []
    for k, v in gearMap.items():
        if len(v) > 1:
            # take product of two elements in set
            res = v.pop() * v.pop()
            products.append(res)
    return products


def determinePartNumberSum(lines):
    grid = build2DArray(lines)
    ROW_MAX, COL_MAX = len(grid), len(grid[0])
    partNumbers = []

    r, c = 0, 0
    while r < ROW_MAX:
        while c < COL_MAX:
            if grid[r][c].isdigit():
                # find entire adjacent number
                numArr, length = findAdjacentNumber(grid, r, c)

                # check all elements around element gric[r][c] with number length
                isPartNumber = checkAllAdjacent(grid, r, c, numArr, length)

                if isPartNumber:
                    partNumbers.append(int("".join(numArr)))

                c += length
                continue

            c += 1

        c = 0
        r += 1

    filteredMap = removeDups(gearMap)
    products = parseMap(filteredMap)
    return sum(products)


if __name__ == "__main__":
    with open("aoc3_input.txt", "r") as i_file:
        i_file = i_file.read()
        lines = i_file.splitlines()
        print(determinePartNumberSum(lines))
