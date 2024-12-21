import re

numberMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# sliding window approach - didn't work out
def includeStringNums(i_file):
    res = []
    for line in i_file.splitlines():
        subRes = []
        start = 0
        for end in range(0, len(line)):
            subStr = line[start : end + 1].lower()

            if subStr in numberMap:
                subRes.append(str(numberMap[subStr]))
                start = end + 1
                continue

            if line[end].isdigit():
                subRes.append(line[end])
                start += 1
                continue

        res.append(int(subRes[0] + subRes[-1]))

    return sum(res)


def includeStringNumsRegex(i_file):
    res = []
    regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    pattern = re.compile(regex)

    for line in i_file.splitlines():
        subRes = []
        for match in pattern.findall(line):
            if match in numberMap:
                subRes.append(str(numberMap[match]))
            else:
                subRes.append(match)
        res.append(int(subRes[0] + subRes[-1]))

    return sum(res)


def sumNumberStrings(i_file):
    res = []
    for line in i_file.splitlines():
        subRes = []
        for c in line:
            if c.isdigit():
                subRes.append(c)
        res.append(int(subRes[0] + subRes[-1]))

    return sum(res)


if __name__ == "__main__":
    with open("aoc1_input.txt", "r") as f:
        i_file = f.read()
        # print(sumNumberStrings(i_file))
        print(includeStringNumsRegex(i_file))
