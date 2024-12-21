def getCardNumber(card):
    card = card.split(":")
    card = card[0].split()
    card = card[1]
    return int(card)


def splitCard(card):
    card = card.split(":")
    card = card[1].split("|")

    winning_numbers = card[0].split()
    ticket_numbers = card[1].split()

    w_num = [int(n) for n in winning_numbers]
    t_num = [int(n) for n in ticket_numbers]

    return w_num, t_num


def findMatches(winning_numbers, ticket_numbers):
    matches = 0
    for number in ticket_numbers:
        if number in winning_numbers:
            matches += 1
    return matches


def deterimineWinningCardSum(cards):
    cardMap = {}  # card number -> (copies, matches)

    # initialize cardMap
    for c in cards:
        card_number = getCardNumber(c)
        winning_numbers, ticket_numbers = splitCard(c)
        matches = findMatches(winning_numbers, ticket_numbers)
        cardMap[card_number] = (1, matches)

    # determine copies for each card
    for k, v in cardMap.items():
        card = k
        copies, matches = v
        for _ in range(copies):
            for m in range(1, matches + 1):
                c, ma = cardMap[card + m]
                cardMap[card + m] = (c + 1, ma)

    # determine total copies
    total_copies = 0
    for k, v in cardMap.items():
        copies, matches = v
        total_copies += copies

    return total_copies


if __name__ == "__main__":
    with open("aoc4_input.txt", "r") as i_file:
        i_file = i_file.read()
        lines = i_file.splitlines()
        print(deterimineWinningCardSum(lines))
