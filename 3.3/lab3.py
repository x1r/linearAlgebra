INFINITY = round(1e69)


class xyz(object):
    def __init__(cls, *args):
        cls.x, cls.y, cls.z = args


class ray(object):
    def __init__(cls, *args):
        cls.origin, cls.direction = args

    def representation_of(cls, pl):
        if pl.intersection(cls) == -INFINITY:
            return -INFINITY
        return ray(pl.intersection(cls), cls.direction.vector_projection_on(pl.to_vector()) * (-2) + cls.direction)

    def __str__(cls) -> str:
        return "{0} {1} \n".format(cls.direction, cls.origin)

    def __add__(cls, other):
        return ray(cls.origin + other, cls.direction + other)

    def __mul__(cls, other):
        return ray(cls.origin * other, cls.direction * other)

    def __sub__(cls, other):
        return ray(cls.origin - other, cls.direction - other)


class plane(object):
    def __init__(cls, *args):
        cls.a, cls.b, cls.c, cls.d = args

    def __str__(cls) -> str:
        return f"{cls.a} {cls.b} {cls.c} {cls.d} \n"

    def to_vector(cls):
        return vector(cls.a, cls.b, cls.c)

    def intersection(cls, _ray):
        if (
                cls.a * _ray.direction.x + cls.b * _ray.direction.y + cls.c * _ray.direction.z) != 0:
            smth = -(cls.a * _ray.origin.x + cls.b * _ray.origin.y + cls.c * _ray.origin.z + cls.d) / (
                    cls.a * _ray.direction.x + cls.b * _ray.direction.y + cls.c * _ray.direction.z)
        else:
            smth = -INFINITY
        return vector(_ray.direction.x * smth + _ray.origin.x, _ray.direction.y * smth + _ray.origin.y,
                      _ray.direction.z * smth + _ray.origin.z) if smth > 0 else -INFINITY


class vector(object):

    def __init__(cls, *args):
        cls.x, cls.y, cls.z = args
        cls.length = cls.x ** 2 + cls.y ** 2 + cls.z ** 2

    def __add__(cls, other):
        return vector(cls.x + other.x, cls.y + other.y, cls.z + other.z)

    def __sub__(cls, other):
        return vector(cls.x - other.x, cls.y - other.y, cls.z - other.z)

    def __mul__(cls, other):
        return cls.x * other.x + cls.y * other.y + cls.z * other.z if isinstance(other, vector) else vector(
            cls.x * other, cls.y * other, cls.z * other)

    def __str__(cls) -> str:
        return f"{cls.x} {cls.y} {cls.z} \n"

    def len(cls):
        return cls.length ** 0.5

    def vector_projection_on(cls, other):
        return other * ((cls * other) / other.length)


def plane_set(_a: xyz, _b: xyz, _c: xyz):
    a = _b.z * (_a.y - _c.y) + _c.y * _a.z + _b.y * (_c.z - _a.z) - _c.z * _a.y
    b = _a.x * (_c.z - _b.z) + _a.z * (_b.x - _c.x) - _b.x * _c.z + _b.z * _c.x
    c = _a.y * (_a.x - _b.x) + _a.x * (_b.y - _a.y) + _b.x * _a.y - _b.y * _a.x
    d = -(_a.x * a + _a.y * b + _a.z * c)
    return plane(a, b, c, d)


def solution():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    _a = vector(*map(float, input_file.readline().split()))
    _b = vector(*map(float, input_file.readline().split()))
    _c = vector(*map(float, input_file.readline().split()))
    _d = vector(*map(float, input_file.readline().split()))
    _e = vector(*map(float, input_file.readline().split()))
    _ray = ray(vector(*map(float, input_file.readline().split())), _e)
    _energy = int(input_file.readline())
    _n = int(input_file.readline())
    _vector = [_b - _a, _d - _c]
    _faces = [
        plane_set(_a, _b, _c), plane_set(_d, _b, _c),
        plane_set(_a, _b, _b + _vector[1]), plane_set(_a, _c - _vector[0], _d - _vector[0]),
        plane_set(_c - _vector[0], _c, _d), plane_set(_a + _vector[1], _b + _vector[1], _d)
    ]
    _mirrors = [plane_set(vector(*map(float, input_file.readline().split())),
                          vector(*map(float, input_file.readline().split())),
                          vector(*map(float, input_file.readline().split()))) for _ in range(_n)]
    _flag = 0
    while _energy > 0:
        _temp_result = [-1, -INFINITY, -1]
        for mirror in _mirrors:
            _t = _ray.representation_of(mirror)
            if _t != -INFINITY and (_temp_result[0] == -1 or _temp_result[0] > (_t.origin - _ray.origin).len() > 0):
                _temp_result = [(_t.origin - _ray.origin).len(), _t, 0]

        for face in _faces:
            _t = _ray.representation_of(face)
            if _t != -INFINITY and (_temp_result[0] == -1 or _temp_result[0] > (_t.origin - _ray.origin).len() > 0):
                _temp_result = [(_t.origin - _ray.origin).len(), _t, 1]

        if _temp_result[2] == -1:
            _flag = 1
            break
        if _temp_result[2] == 1:
            _flag = 1
            print(f"1\n{str(_energy)}\n{str(_temp_result[1].origin)}{str(_ray.direction)}", file=output_file)
            break
        _ray = _temp_result[1]
        _energy -= 1

    if not _flag:
        print(f"0\n{str(_ray.origin)}\n{str(_ray.direction)}\n", file=output_file)
        output_file.close()


def check_solution():
    with open("output.txt", 'r') as f:
        for line in f:
            print(line.strip())


if __name__ == '__main__':
    ##  Linux-styled Art for A. Serdyukov by ξ𝕽 © 2022
    ##
    ##           _nnnn_
    ##          dGGGGMMb     ,"""""""""""""".
    ##         @p~qp~~qMb    | BIT Rules!   |
    ##         M|@||@) M|   _;..............'
    ##         @,----.JM| -'
    ##        JS^\__/  qKL
    ##       dZP        qKRb
    ##      dZP          qKKb
    ##     fZP            SMMb
    ##     HZM            MMMM
    ##     FqM            MMMM
    ##   __| ".        |\dS"qML
    ##   |    `.       | `' \Zq
    ##  _)      \.___.,|     .'
    ##  \____   )MMMMMM|   .'
    ##       `-'       `--'
    ##
    solution()
