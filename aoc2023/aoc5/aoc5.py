def getSeedList(seedLine):
    seeds = []
    seedLine = seedLine.split(":")[1].strip()
    for s in seedLine.split(" "):
        seeds.append(int(s))
    return seeds


def getSeedListPart2(seedLine):
    seeds = []
    seedLine = seedLine.split(":")[1].strip()
    seedsArr = seedLine.split(" ")
    s_i = 0
    while s_i < len(seedsArr):
        s, r = int(seedsArr[s_i]), int(seedsArr[s_i + 1])
        for i in range(s, s + r):
            seeds.append(i)
        s_i += 2
    return seeds


def parseMapDefinitions(lines):
    maps = []
    maps_str = "\n".join(lines).split("\n\n")

    for m in maps_str:
        # maps.append(parseMap(m))
        maps.append(getRanges(m))

    return maps


def getRanges(map_definition):
    # part 1: generating ranges
    ranges = []
    map_str = map_definition.split("\n")
    map_str = map_str[1:]

    for m in map_str:
        d, s, r = m.split(" ")
        range_info = [int(d), int(s), int(r)]
        ranges.append(range_info)

    return ranges


def parseMap(map_definition):
    # part 2: generating maps
    res_map = {}
    map_str = map_definition.split("\n")
    map_str = map_str[1:]

    for m in map_str:
        d, s, r = m.split(" ")
        d, s, r = int(d), int(s), int(r)
        for i in range(s, s + r):
            res_map[i] = d
            d += 1

    return res_map


def findLocation(seed, maps):
    for m in maps:
        # in part 1, we just indexed the map to get the value
        # part 2: using ranges
        for ra in m:
            d, s, r = ra
            if s <= seed <= s + r:
                seed += d - s
                break

    return seed


def determineLowestSeedLocation(lines):
    # high level plan:
    # 1. parse the seed line, put seeds into a list
    locations = []
    # seeds = getSeedList(lines[0])
    seeds = getSeedListPart2(lines[0])

    # 2. parse the map definitions
    # 3. build each map, correctly
    maps = parseMapDefinitions(lines[2:])

    # 4. loop through seeds, and iteratively find the seed location through the various maps
    # 5. place seed locations into a list
    for s in seeds:
        loc = findLocation(s, maps)
        locations.append(loc)

    # 6. return the lowest seed location
    return min(locations)


if __name__ == "__main__":
    with open("aoc5_input.txt", "r") as i_file:
        i_file = i_file.read()
        lines = i_file.splitlines()
        print(determineLowestSeedLocation(lines))
