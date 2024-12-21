# Game X: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# parse the above screen so we get a data structure like this:
# (1, [[3, 4, 0], [1, 0, 2], [0, 2, 0]])
def getCubeResults(line):
    gameNum = int(line.split(":")[0].split(" ")[1])
    strWithoutGameNum = line.split(":")[1].strip()
    rounds = strWithoutGameNum.split(";")

    res = []
    for r in rounds:
        subR = [0] * 3
        r = r.strip().split(", ")

        for n in r:
            n, color = n.split(" ")
            if color == "red":
                subR[0] = int(n)
            elif color == "green":
                subR[1] = int(n)
            else:
                subR[2] = int(n)
        res.append(subR)

    return (gameNum, res)


def findAllPossibleGames(lines):
    redCubes, greenCubes, blueCubes = 12, 13, 14  # total cubes
    possibleGames = []

    for l in lines:
        gameNum, rounds = getCubeResults(l)

        upperR = []
        for r in rounds:
            subR = []
            for i, c in enumerate(r):
                if i == 0:
                    if c > redCubes:
                        subR.append("L")
                elif i == 1:
                    if c > greenCubes:
                        subR.append("L")
                elif i == 2:
                    if c > blueCubes:
                        subR.append("L")

            if len(subR) == 0:
                upperR.append("W")

        if len(upperR) == len(rounds):
            possibleGames.append(gameNum)
    return sum(possibleGames)


def findSummationOfPower(lines):
    redCubes, greenCubes, blueCubes = 12, 13, 14  # total cubes
    powersPerGame = []

    for l in lines:
        maxRed, maxGreen, maxBlue = 0, 0, 0
        gameNum, rounds = getCubeResults(l)
        print(rounds)

        for r in rounds:
            for i, c in enumerate(r):
                if i == 0:
                    maxRed = max(maxRed, c)
                elif i == 1:
                    maxGreen = max(maxGreen, c)
                elif i == 2:
                    maxBlue = max(maxBlue, c)

        powersPerGame.append(maxRed * maxGreen * maxBlue)

    return sum(powersPerGame)


if __name__ == "__main__":
    with open("aoc2_input.txt", "r") as f:
        i_file = f.read()
        lines = i_file.splitlines()
        print(findAllPossibleGames(lines))
        print(findSummationOfPower(lines))
