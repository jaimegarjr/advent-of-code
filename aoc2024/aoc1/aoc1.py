from collections import Counter


def findDistance(first, second):
    first.sort()
    second.sort()
    distances = []
    print(first, second)
    for f, s in zip(first, second):
        dist = abs(f - s)
        print(f"f: {f}, s: {s}, distance: {dist}")
        distances.append(dist)

    return sum(distances)


def findSimilarity(first, second):
    scores = []
    s_occurences = Counter(second)
    for f, s in zip(first, second):
        multiple = s_occurences[f]
        similarity_score = f * multiple
        scores.append(similarity_score)

    return sum(scores)


if __name__ == "__main__":
    with open("aoc1_input.txt", "r") as f:
        lines = f.readlines()

    first = []
    second = []
    for l in lines:
        newLine = l.strip()
        one, two = newLine.split()
        first.append(int(one))
        second.append(int(two))

    # res = findDistance(first, second)
    res = findSimilarity(first, second)
    print(res)
