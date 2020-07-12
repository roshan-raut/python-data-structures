def find_uppercase_iterative(str):
    for i in range(len(str)):
        if str[i].isupper():
            return str[i]
    return "No uppercase character found"


def find_uppercase_recursive(str, idx=0):
    if str[idx].isupper():
        return str[idx]
    if idx == len(str) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(str, idx+1)

input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))