finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#N
#N/2
#N/4
#N/8...
#N/2^K
# 2^k = N
# k = log_2(N)
#k번 탐샛을 하면 원하는 딱 1개의 원소를 찾을 수 있다.

# O(log(N))

def is_existing_target_number_binary(target, array):
    find_count = 0
    cur_min = 0
    cur_max = len(array)-1
    cur_guess = (cur_min+cur_max)//2

    while cur_min <= cur_max:
        find_count+=1
        if array[cur_guess] == target:
            print(find_count) # 3번 걸림
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess+1
        else:
            cur_max = cur_guess-1
        cur_guess = (cur_min+cur_max)//2
    return False



result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)