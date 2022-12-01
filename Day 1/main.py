import os


def get_amount_per_elf() -> list[int]:
    # open file input.txt
    with open(os.path.join(os.getcwd(), "Day 1\\input.txt")) as f:
        lines = f.readlines()
        amount_per_elf = []
        my_sum = 0
        for line in lines:
            if line != "\n":
                my_sum += int(line)
            else:
                amount_per_elf.append(my_sum)
                my_sum = 0
    return amount_per_elf


def get_top_three():
    amount_per = get_amount_per_elf()
    amount_per.sort(reverse=True)
    my_sum = 0
    for i in range(3):
        print(amount_per[i])
        my_sum += amount_per[i]
    print(my_sum)


def get_max():
    amount_per = get_amount_per_elf()
    print(max(amount_per))


if __name__ == "__main__":
    get_max()
    get_top_three()
