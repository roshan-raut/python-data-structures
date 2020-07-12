# Iterative length calculation: O(n)
def iterative_str_len(str):
    str_len = 0
    for i in range(len(str)):
        str_len += 1
    return str_len


# Recursive length calculation: O(n)
def recursive_str_len(str):
    if str == "":
        return 0
    return 1 + recursive_str_len(str[1:])


input_str = "LucidProgramming"

print(iterative_str_len(input_str))
print(recursive_str_len(input_str))