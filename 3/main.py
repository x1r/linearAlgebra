def get_answer(data: list) -> str:
    """
    1. unpack data from file
    2. solve equation
    3. create string from list
    4. return string
    """
    x1, y1, x2, y2, value1, value2 = data
    answer = solve_system_of_equations_2x2(x1, y1, x2, y2, value1, value2)
    # return " ".join(map(str, answer))
    string = ""
    for element in answer:
        string += str(element) + " "
    return string.rstrip()


def solve_system_of_equations_2x2(x1, y1, x2, y2, value1, value2) -> list:
    """
    If I was paid for every if statement I wrote, I would be a millionaire.©🤡
    Output:
    0 - no solution                  |  V
    1 - infinitely many solutions    |  V
    2 - one solution                 |  V
    3 - x = x0, y0 - any             |  V
    4 - y = y0, x0 - any             |  V
    5 - anything is a solution       |  V
    """
    if x1 == y1 == x2 == y2 == 0 and (value1 != 0 or value2 != 0):
        return [0]
    # 2 - one solution
    # using Kramer method for finding x and y
    if x1 * y2 - x2 * y1 != 0:
        x = (y2 * value1 - y1 * value2) / (x1 * y2 - x2 * y1)
        y = (x1 * value2 - x2 * value1) / (x1 * y2 - x2 * y1)
        return [2, x, y]
    if x1 * y1 * x2 * y2 * value1 * value1 == 0:
        # 5 - anything is a solution
        if x1 == y1 == x2 == y2 == value1 == value1 == 0:
            # collapser
            return [5]
        # 1 or 3 or 4 or no solution
        if x1 == y1 == 0:
            if value1 == 0:
                if y2 == 0:
                    if x2 == 0:
                        if value2 != 0:
                            return [0]
                    else:
                        return [3, value2 / x2]
                if x2 == 0:
                    if y2 == 0:
                        if value2 != 0:
                            return [0]
                    else:
                        return [4, value2 / y2]
                return [1, -x2 / y2, value2 / y2]
            return [0]
        if x2 == y2 == 0:
            if value2 == 0:
                if y1 == 0:
                    if x1 == 0:
                        if value1 != 0:
                            return [0]
                    else:
                        return [3, value1 / x1]
                if x1 == 0:
                    if y1 == 0:
                        if value1 != 0:
                            return [0]
                    else:
                        return [4, value1 / y1]
                return [1, -x1 / y1, value1 / y1]
            return [0]
        # 3 - x = x0, y0 - any
        if y1 == y2 == 0:
            if x1 == 0 and value1 == 0:
                if x2 == 0 and value2 != 0:
                    return [0]
                return [3, value2 / x2]
            if x2 == 0 and value2 == 0:
                if x1 == 0 and value1 != 0:
                    return [0]
                return [3, value1 / x1]
            if x1 == 0 and value1 != 0:
                return [0]
            if x2 == 0 and value2 != 0:
                return [0]
            if (x1 == value2 == 0 and x2 != 0 and value1 != 0) or (x2 == value1 == 0 and x1 != 0 and value2 != 0):
                return [0]
            if x1 != 0 and value1 == 0:
                return [3, 0] if value2 == 0 else [0]
            if x2 != 0 and value2 == 0:
                return [3, 0] if value1 == 0 else [0]
            if value1 / x1 == value2 / x2:
                return [3, value1 / x1]
            return [0]
        # 4 - y = y0, x0 - any
        if x1 == x2 == 0:
            if y1 == 0 and value1 == 0:
                if y2 == 0 and value2 != 0:
                    return [0]
                return [4, value2 / y2]
            if y2 == 0 and value2 == 0:
                if y1 == 0 and value1 != 0:
                    return [0]
                return [4, value1 / y1]
            if y1 == 0 and value1 != 0:
                return [0]
            if y2 == 0 and value2 != 0:
                return [0]
            if (y1 == value2 == 0 and y2 != 0 and value1 != 0) or (y2 == value1 == 0 and y1 != 0 and value2 != 0):
                return [0]
            if y1 != 0 and value1 == 0:
                return [4, 0] if value2 == 0 else [0]
            if y2 != 0 and value2 == 0:
                return [4, 0] if value1 == 0 else [0]
            if value1 / y1 == value2 / y2:
                return [4, value1 / y1]
            return [0]
        if value1 == value2 == 0:
            if x2 != 0 and y2 != 0:
                if x1 / x2 == y1 / y2:
                    return [1, -x1 / y1, 0]
            if x1 != 0 and y1 != 0:
                if x2 / x1 == y2 / y1:
                    return [1, -x2 / y2, 0]
    # 1 - infinitely many solutions
    if value2 != 0:
        if x1 / x2 == y1 / y2 == value1 / value2:
            return [1, -x1 / y1, value1 / y1]
    if value1 != 0:
        if x2 / x1 == y2 / y1 == value2 / value1:
            return [1, -x2 / y2, value2 / y2]
    # 1, 3, 4
    if x1 * x2 * y1 * y2 != 0:
        if x1 / x2 != y1 / y2:
            if x1 == x2:
                return [4, value1 / y1]
            if y1 == y2:
                return [3, value1 / x1]
    return [0]


def main():
    with open("input.txt") as input_file, open("output.txt", "w") as output_file:
        data_from_file = map(float, input_file.readline().split())
        output_file.write(get_answer(data_from_file))


if __name__ == "__main__":
    main()


# with open("input.txt", mode="rt") as f:
#     a, b, c, d, p, q = map(float, f.readline().split())
# letters = [a, b, c, d]
# ans = [0]
# if a*d-b*c != 0:
#     ans = [2, (p*d - b*q)/(a*d-b*c), (a*q - p*c)/(a*d-b*c)]
# elif a==0 and c==0 and b!=0 and d!=0 and p/b == q/d:
#     ans = [4, q/d]
# elif b == 0 and d == 0 and a!=0 and c!=0 and p/a == q/c:
#     ans = [3, p/a]
# elif b*q*c == p*d*c == a*q*d and a!=0 and b!= 0 and c!=0 and d!=0:
#     ans = [1, -a/b, p/b]
# elif a!=0 and b!=0 and c == 0 and d == 0 and q==0:
#     ans = [1, -a/b, p/b]
# elif c!=0 and d!= 0 and a==0 and b==0 and p == 0:
#     ans = [1, -c/d, q/d]
# elif a == b == c == d == p == q == 0:
#     ans = [5]
# # letters = [a, b, c, d]
# elif letters.count(0) == 3:
#     for i in range(4):
#         if letters[i] != 0:
#             if i == 0 and q == 0:     if a!=0 and q=0
#                 ans = [3, p/letters[i]]
#             elif i == 1 and q == 0:   if b!=0 and q=0
#                 ans = [4, p/letters[i]]
#             elif i == 2 and p == 0:   if c!=0 and p=0
#                 ans = [3, q/letters[i]]
#             elif i == 3 and p == 0:   if d!=0 and p=0
#                 ans = [4, q/letters[i]]
#
# with open("output.txt", "w") as f:
#     f.write(f"{' '.join(map(str, ans))}")