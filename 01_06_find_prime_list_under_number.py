# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.

input = 20

def find_prime_list_under_number(number):
    arr=[]

    # 문제 해결 2
    # for num in range(2,number+1):
    #     for i in arr:  # 효율적
    #     # for i in range(2, num): 비 효율적
    #         if i * i <= num and num % i == 0:
    #             break
    #     else:
    #         arr.append(num)
    # print(arr)


    # 문제 해결 1
    # for num in range(2,number+1):
    #     is_prime = True
    #     for i in range(2, int(num ** 0.5) + 1):
    #         if(num % i)==0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         arr.append(num)
    # print(arr)

result = find_prime_list_under_number(input)
print(result)