def longest_uniform_substring(s):
    max_len = 1
    current_len = 1
    prev_char = s[0]

    for char in s[1:]:
        if char == prev_char:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
            prev_char = char

    max_len = max(max_len, current_len)

    return max_len

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)  # Output: 4

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)  # Output: 1
