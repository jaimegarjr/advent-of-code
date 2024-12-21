def determineSafeReport(report):
    safe = True

    is_increasing = report[0] < report[-1]
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if is_increasing:
            if abs(diff) > 3 or report[i] < report[i - 1] or diff == 0:
                safe = False
                break
        else:
            if abs(diff) > 3 or report[i] > report[i - 1] or diff == 0:
                safe = False
                break

    return safe


def findSafeReports(reports):
    safe_reports = 0
    for report in reports:
        safe = determineSafeReport(report)
        if safe:
            safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    with open("aoc2_input.txt", "r") as f:
        lines = f.readlines()

    reports = []
    for l in lines:
        level = l.strip()
        digits = level.split()
        # convert to integers
        digits = [int(d) for d in digits]
        reports.append(digits)

    res = findSafeReports(reports)
    print(res)
