import re

def filterInput(input_str):
    instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input_str)
    return instructions

def performMultiplications(instructions):
    total = 0

    for i in instructions:
        values = re.findall(r"[0-9]{1,3}", i)
        n, m = int(values[0]), int(values[1])
        total += n * m

    return total


if __name__ == "__main__":
    with open("aoc3_input.txt", "r") as f:
        input_data = f.read().strip()

    # should return ['mul(x,y)', etc.]
    mul_instructions = filterInput(input_data)
    res = performMultiplications(mul_instructions)
    print(res)

