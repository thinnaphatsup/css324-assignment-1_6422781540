def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4 and s[2] == 0

def successors(s):
    a, b, c = s
    successors_array = []

    if a > 0 and b < 5:
        minpourpertime = min(a, 5 - b)
        successors_array.append(((a - minpourpertime, b + minpourpertime, c), minpourpertime))

    if a > 0 and c < 3:
        minpourpertime = min(a, 3 - c)
        successors_array.append(((a - minpourpertime, b, c + minpourpertime), minpourpertime))

    if b > 0 and a < 8:
        minpourpertime = min(b, 8 - a)
        successors_array.append(((a + minpourpertime, b - minpourpertime, c), minpourpertime))

    if b > 0 and c < 3:
        minpourpertime = min(b, 3 - c)
        successors_array.append(((a, b - minpourpertime, c + minpourpertime), minpourpertime))

    if c > 0 and a < 8:
        minpourpertime = min(c, 8 - a)
        successors_array.append(((a + minpourpertime, b, c - minpourpertime), minpourpertime))

    if c > 0 and b < 5:
        minpourpertime = min(c, 5 - b)
        successors_array.append(((a, b + minpourpertime, c - minpourpertime), minpourpertime))

    return successors_array