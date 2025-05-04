def find_max_occurred_alphabet(string):

    # 문제 해결 2
    alphabet_index = [0]*26
    max_occurred_alphabet = ""
    max_occurrences = 0
    for char in string:
        if not char.isalpha():
            continue
        alphabet_index[ord(char) - 97] += 1
    print(alphabet_index)
    for index in range(len(alphabet_index)):
        if alphabet_index[index] > max_occurrences:
            max_occurrences = alphabet_index[index]
            max_occurred_alphabet = index
    return chr(max_occurred_alphabet+97)


    # 문제 해결 1
    # alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    #                   "t", "u", "v", "w" , "x", "y", "z"]
    # print(len(alphabet_array))
    # max_occurred_alphabet = ""
    # max_occurrences = 0
    # for alphabet in alphabet_array:
    #     occurrences = 0
    #     for char in string:
    #         if not char.isalpha():
    #             continue
    #         if char in alphabet:
    #             occurrences += 1
    #     if max_occurrences < occurrences:
    #           max_occurrences = occurrences
    #           max_occurred_alphabet = alphabet
    # print(max_occurred_alphabet, max_occurrences)
    #
    # return max_occurred_alphabet


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))