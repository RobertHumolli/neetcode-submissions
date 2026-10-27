from typing import List

def read_integers() -> List[int]:
    numbers = input()

    numbers_line = numbers.split(',')
    new_list = []

    for i in numbers_line:
        new_list.append(int(i))

    return new_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
