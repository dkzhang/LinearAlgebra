from palyLA.Vector import Vector

if __name__ == "__main__":
    vec1 = Vector([5, 2])
    print(vec1)
    print(len(vec1))
    print("vec[0] = {}, vec[1] = {}".format(vec1[0], vec1[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec1, vec2, vec1 + vec2))
    print("{} - {} = {}".format(vec1, vec2, vec1 - vec2))

    print("{} * {} = {}".format(vec1, 3, vec1 * 3))
    print("{} * {} = {}".format(3, vec1, 3 * vec1))

    print("+{} = {}".format(vec1, +vec1))
    print("-{} = {}".format(vec1, -vec1))

    zero2 = Vector.zero(2)
    print(zero2)
    print("{} + {} = {}".format(vec1, zero2, vec1 + zero2))
