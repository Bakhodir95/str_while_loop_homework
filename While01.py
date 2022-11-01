
"""
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """


def main(s):

    i = 0
    count = ""

    while i < len(s):
        if s[i].isdigit():
            count += s[i]
        i += 1

    count = len(count)
    return count


print(main("4t54t4fgr"))
