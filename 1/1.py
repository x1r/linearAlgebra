def horner(xzero: int, coefficients: list) -> int:
    result = 0
    for coefficient in coefficients:
        result = result * xzero + coefficient
    return result

def main():
    with open("input.txt") as fIn:
        fIn.readline()
        coefficients, xzero = list(map(int, fIn.readline().split())), int(fIn.readline())
        with open("output.txt", "w") as fOut:
            fOut.write(str(horner(xzero, coefficients)))


if __name__ == "__main__":
    main()
