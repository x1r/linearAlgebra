from math import fabs, sqrt, acos, atan, degrees


def length(x: float, y: float, z: float) -> float:
    return sqrt(x ** 2 + y ** 2 + z ** 2)


def angle(a: float, b: float, c: float, x: float, y: float, z: float) -> float:
    return degrees(acos(round((a * x + b * y + c * z) / (length(a, b, c) * length(x, y, z)), 2)))


def angle_2d(a: float, b: float, c: float, d: float) -> float:
    return degrees(acos(float((a * c + b * d) / (sqrt(a ** 2 + b ** 2) * sqrt(c ** 2 + d ** 2)))))


def dot_product_2d(x: list[float], y: list[float]) -> float:
    return sum(x[i] * y[i] for i in range(2))


def minus_vector(a: float, b: float, x: float, y: float) -> float:
    return a * b - x * y


def multiply_vectors(x: list[float], y: list[float]) -> list:
    return [minus_vector(x[1], y[2], x[2], y[1]), minus_vector(x[2], y[0], x[0], y[2]),
            minus_vector(x[0], y[1], x[1], y[0])]


def dot_product(x: list[float], y: list[float]) -> float:
    return x[0] * y[0] + x[1] * y[1] + x[2] * y[2]


def beam_check(v: list[float], a: list[float], elv: list[float]) -> float:
    if elv[0] == v[0] and elv[1] == v[1]:
        return 1
    if a[0] == 0:
        return 1 if (elv[0] <= v[0] and a[1] > 0) or (elv[0] > v[0] and a[1] <= 0) else -1
    elif a[0] != 0:
        k1 = a[1] / a[0]
        k2 = k1 * (elv[0] - v[0]) + v[1]
        if k1 > 0:
            return 1 if (elv[1] > k2 and a[0] > 0) or (elv[1] <= k2 and a[0] <= 0) else -1
        else:
            return 1 if (elv[1] > k2 and a[0] > 0) or (elv[1] <= k2 and a[0] <= 0) else -1


def keel_angle(v: list[float], a: list[float], m: list[float], w: list[float]) -> float:
    alpha = 90
    enemy = [w[i] - v[i] for i in range(3)]
    enemy[2] = dot_product_2d(v, m) - dot_product_2d(w, m)
    if enemy[2] < 0:
        return alpha
    a[2] = -dot_product_2d(a, m)
    if all(m[i] == 0 for i in range(2)):
        if (a[0] != enemy[0] or a[1] != enemy[1]) and (a[0] != -enemy[0] or a[1] != -enemy[1]):
            return alpha - angle_2d(a[0], a[1], enemy[0], enemy[1])
    else:
        if any(enemy[i] != a[i] for i in range(3)) or any(enemy[i] != -a[i] for i in range(3)):
            return alpha - angle(*a, *enemy)
    return alpha


def mast_angle(mv: list[float]) -> float:
    if all(i == 0 for i in mv[0:2]):
        return 0
    return 90 - degrees(atan(1 / sum(mv[i] ** 2 for i in range(2)) ** (1 / 2)))


def solution():
    with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
        radius_vector = list(map(float, input_file.readline().split()))
        keel_vector = list(map(float, input_file.readline().split()))
        mast_vector = list(map(float, input_file.readline().split()))
        enemy_location_vector = list(map(float, input_file.readline().split()))
        radius_vector.append(float(0))
        keel_vector.append(float(0))
        mast_vector.append(float(1))
        enemy_location_vector.append(float(0))

        beta = mast_angle(mast_vector)

        beam = beam_check(radius_vector, keel_vector, enemy_location_vector)
        alpha = keel_angle(radius_vector, keel_vector, mast_vector, enemy_location_vector)
        # print(beam, alpha, beta)
        if all(radius_vector[i] == enemy_location_vector[i] for i in range(2)):
            print(f"1\n{0}\n{beta}")
        if fabs(alpha) <= 60:
            if fabs(beta) > 60:
                print(f"0\n{alpha:.2f}\n{beta:.2f}", file=output_file)
            else:
                print(f"{beam}\n{alpha:.2f}\n{beta:.2f}", file=output_file)
        else:
            print(f"0\n{alpha:.2f}\n{beta:.2f}", file=output_file)
        output_file.write("Depression")


def main():
    solution()


if __name__ == "__main__":
    main()
