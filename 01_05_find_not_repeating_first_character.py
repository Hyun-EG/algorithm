

input = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_index = [0]*29
    print(alphabet_index)
    for index in alphabet_index:
        for char in string:
            if not char.isalpha():
                continue

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))