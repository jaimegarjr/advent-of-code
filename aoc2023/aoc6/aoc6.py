def parseRaces(lines):
    times_str = lines[0].split(":")[1].strip()
    distance_str = lines[1].split(":")[1].strip()

    distances = [int(d) for d in distance_str.split()]
    times = [int(t) for t in times_str.split()]

    return times, distances


def parseRacesPart2(lines):
    times_str = lines[0].split(":")[1].strip()
    distance_str = lines[1].split(":")[1].strip()

    distance = [int("".join(distance_str.split()))]
    time = [int("".join(times_str.split()))]

    return time, distance


def determineProductOfTotalWins(lines):
    times, distances = parseRacesPart2(lines)
    res = []

    for t, d in zip(times, distances):
        wins = 0
        for i in range(t + 1):
            dis = i * (t - i)
            if dis > d:
                wins += 1
        res.append(wins)

    product = 1
    for r in res:
        product *= r
    return product


if __name__ == "__main__":
    with open("aoc6_input.txt", "r") as i_file:
        i_file = i_file.read()
        lines = i_file.splitlines()
        print(determineProductOfTotalWins(lines))
