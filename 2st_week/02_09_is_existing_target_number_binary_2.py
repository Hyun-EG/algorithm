finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    sorted_array = sorted(array)
    min_cur = 0
    max_cur = len(sorted_array)-1
    cur_guess = (max_cur+min_cur)//2
    while min_cur<=max_cur:
        if target == sorted_array[cur_guess]:
            return True
        elif target < sorted_array[cur_guess]:
            max_cur = cur_guess-1
        else:
            min_cur = cur_guess+1
        cur_guess = (max_cur+min_cur)//2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)