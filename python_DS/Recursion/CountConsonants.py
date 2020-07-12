vowels = "aeiou"


def iterative_count_consonants(str):
    consonant_count = 0
    for i in range(len(str)):
        if str[i].lower() not in vowels and str[i].isalpha():
            consonant_count += 1
    return consonant_count


def recursive_count_consonants(str, index=0):
    if str == "":
        return 0
    if str[index].lower() not in vowels and str[index].isalpha():
        return 1 + recursive_count_consonants(str[1:])
    return recursive_count_consonants(str[1:])


input_str = "abc de"
print(input_str)
print(iterative_count_consonants(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(recursive_count_consonants(input_str))