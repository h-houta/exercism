def square(grain):
    if not 1 <= grain <= 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (grain - 1)


def total():
    return (1 << 64) - 1
