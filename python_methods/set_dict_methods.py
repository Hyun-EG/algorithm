#set() : 중복되는 값을 제거하고 유니크 값만 놨둠 (정렬x)
set_name = ['박','성','현','현','성','성']
print(set(set_name)) # {'현', '성', '박'} << 순서는 무작위로 나온거
# 돌리면 다시 새롭게 나옴
# 중복되는 값만 유니크 값으로 바꿔주지 정렬은 안해줌

#dict_fromkeys() : 중복되는 값을 제거하고 유니크 값만 놨둠 (정렬o)
dict_fromkeys_name = ['박','성','현','현','성','성']
unique_name = list(dict.fromkeys(dict_fromkeys_name))
print(unique_name) # ['박','성','현']

