import os


def get_input() -> list[int]:
    # open file input.txt
    with open(os.path.join(os.getcwd(), "Day 2/input.txt")) as f:
        # read file and split by new line
        lines = f.readlines()
    return lines


def remove_newline_char(input: list[int]) -> list[int]:
    return [line.replace("\n", "") for line in input]


def split_input_into_two_lists(input):
    return [(x, y) for (x, y) in [line.split(" ") for line in input]]


def calculate_score_one() -> int:
    score = 0
    round_list = split_input_into_two_lists(remove_newline_char(get_input()))
    for x, y in round_list:
        match x, y:
            case "A", "X":
                score += 1 + 3
            case "A", "Y":
                score += 2 + 6
            case "A", "Z":
                score += 3 + 0
            case "B", "X":
                score += 1 + 0
            case "B", "Y":
                score += 2 + 3
            case "B", "Z":
                score += 3 + 6
            case "C", "X":
                score += 1 + 6
            case "C", "Y":
                score += 2 + 0
            case "C", "Z":
                score += 3 + 3
    return score


def calculate_score_two() -> int:
    score = 0
    round_list = split_input_into_two_lists(remove_newline_char(get_input()))
    for x, y in round_list:
        match y:
            case "X":
                score += 0
                match x:
                    case "A":
                        score += 3
                    case "B":
                        score += 1
                    case "C":
                        score += 2
            case "Y":
                score += 3
                match x:
                    case "A":
                        score += 1
                    case "B":
                        score += 2
                    case "C":
                        score += 3
            case "Z":
                score += 6
                match x:
                    case "A":
                        score += 2
                    case "B":
                        score += 3
                    case "C":
                        score += 1

    return score


if __name__ == "__main__":
    print(calculate_score_two())
