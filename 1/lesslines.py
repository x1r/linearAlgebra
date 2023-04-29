from functools import reduce as func
with open("input.txt") as input_file, open("output.txt", "w") as output_file:
    skip, coefficients, xzero = input_file.readline(), list(map(int, input_file.readline().split())), int(input_file.readline())
    output_file.write(str(func(lambda x, y: x * xzero + y, coefficients)))