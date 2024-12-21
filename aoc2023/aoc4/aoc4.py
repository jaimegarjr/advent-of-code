def splitCard(card):
    card = card.split(":")
    card = card[1].split("|")

    winning_numbers = card[0].split()
    ticket_numbers = card[1].split()

    w_num = [int(n) for n in winning_numbers]
    t_num = [int(n) for n in ticket_numbers]

    return w_num, t_num


def determineScore(winning_numbers, ticket_numbers):
    score = 0
    for number in ticket_numbers:
        if number in winning_numbers:
            if not score:
                score = 1
            else:
                score *= 2
    return score


def deterimineWinningCardSum(cards):
    scores = []

    for card in cards:
        winning_numbers, ticket_numbers = splitCard(card)
        score = determineScore(winning_numbers, ticket_numbers)
        scores.append(score)

    return sum(scores)


if __name__ == "__main__":
    with open("aoc4_input.txt", "r") as i_file:
        i_file = i_file.read()
        lines = i_file.splitlines()
        print(deterimineWinningCardSum(lines))
