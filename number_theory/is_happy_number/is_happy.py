def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True
    has_seen = {}

    while n not in has_seen:
        has_seen[n] = 0
        s = str(n)
        total = 0
        for i in s:
            total += int(i) ** 2
        if total == 1:
            return True
        else:
            n = total
    return False

n = 19
print(isHappy(n))  # Output: True
