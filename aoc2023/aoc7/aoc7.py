from collections import Counter


def parseInput(lines, hands_to_bids):
    for l in lines:
        hand, bid = l.split()
        hand, bid = hand, int(bid)
        hands_to_bids[hand] = bid


def buildMap(hand):
    return Counter(hand)


def rankHands(hands):
    for h in hands:
        h_map = buildMap(h)
        print(h_map)
    return []


def findTotalWinnings(lines):
    # build a dict of hands to bids
    hands_to_bids = {}
    parseInput(lines, hands_to_bids)

    # rank hands based on criteria
    rankedHands = rankHands(hands_to_bids.keys())

    res = 0
    for i, r in enumerate(rankedHands):
        bid = hands_to_bids[r]
        res += bid * (i + 1)

    return res


if __name__ == "__main__":
    with open("aoc7_input.txt", "r") as i_file:
        i_file = i_file.read()
        lines = i_file.splitlines()
        print(findTotalWinnings(lines))
