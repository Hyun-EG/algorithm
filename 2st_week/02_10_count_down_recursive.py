# 재귀 함수 : 탈출 조건을 정해 두는게 중요

def count_down(number):
    print(number)
    if number != 0:
        count_down(number - 1)

count_down(60)