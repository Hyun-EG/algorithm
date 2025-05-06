
# list.append(x) : 리스트 뒤에 입력한 x를 추가
list_append = ['박','성']
list_append.append("현")
print(list_append) #['박','성','현']

# list.insert(i,x) : i번째 인덱스에 입력한 x를 추가
list_insert = ['박','현']
list_insert.insert(1,'성')
print(list_insert) # ['박','성','현']

# list.extend(iterable) : 반복이 가능한 객체만 원본에 이어줌
list_extend_iterable_1 = ['박']
list_extend_iterable_2 = ['성','현']
list_extend_iterable_1.extend(list_extend_iterable_2)
print(list_extend_iterable_1) # ['박','성','현']

#list.remove() : 인자로 입력한 값을 삭제 해줌
list_remove = ['박','성','현']
list_remove.remove('성')
print(list_remove) # ['박','현']

# list.pop() : 마지막 index를 제거 해줌
list_pop = ['박','성','현']
list_pop.pop()
print(list_pop) # ['박','성']

#list.index(x) : x가 몇번째 index 인지 알려줌
list_index = ['박','성','현']
print(list_index.index('성')) # 1

#list.count(x) : x와 동일한 index가 몇개가 있는지 알려줌
list_count =['박','박', '박박', '성','현']
print(list_count.count('박')) # 2

#list.sort(key=기준 함수, reverse=정렬 방향)
#원본 변경됨 , 반환값 없음
list_sort_len = ['park','Hello World', 'seong', 'hyun']
list_sort_len.sort() # ['Hello World', 'hyun', 'park', 'seong']
print(list_sort_len)
list_sort_len.sort(key=len)
print(list_sort_len) # ['park', 'hyun', 'seong', 'Hello World']

list_sort_reverse = ['박','성','현']
list_sort_reverse.sort()
print(list_sort_reverse) # ['박', '성', '현']
list_sort_reverse.sort(reverse=True)
print(list_sort_reverse) # ['현', '성', '박']

#sorted(반복 가능한 객체, key=기준 함수, reverse=정렬 방향)
#원본 유지 , 반환값(정렬된 새로운 리스트)
original_list_1 = ['박','성','현']
original_list_2 = ['박박','성성성','현']
sorted_list_1= sorted(original_list_1, reverse=True)
print(sorted_list_1) # ['현','성','박']
print(original_list_1) # ['박', '성', '현'] 원본 유지됨
sorted_list_2= sorted(original_list_2, key=len, reverse=True)
print(sorted_list_2) # ['성성성', '박박', '현']

#list.reverse() : 순서 반전
list_reverse = ['박','성','현']
list_reverse.reverse()
print(list_reverse) # ['현', '성', '박']

#reversed(list) : 순서 반전 (원본 유지)
original_reversed_list = ['박','성','현']
reversed_list = reversed(original_reversed_list)
print(list(reversed_list)) # ['현','성','박']
print(original_reversed_list) # ['박', '성', '현'] 원본 유지

#sum() : 숫자 리스트 합을 구해줌 max(): 가장 큰값을 구해줌 min(): 가장 작은값을 구해줌
sum_list = [1,2,3]
print(sum(sum_list)) # 6
print(max(sum_list)) # 3
print(min(sum_list)) # 1

#enumerate(list) : 리스트 반복문에서 index와 값을 같이 알수있음
enumerate_list = ['박','성','현']
for index,char in enumerate(enumerate_list):
    print(index,char) # 0 박
                      # 1 성
                      # 2 현

#zip(list1, list2) : 요소에 맞춰서 튜플 형태로 변환 해줌
#한 쪽이 list가 짧을 시 짧은걸 기준 으로 맞춰줌
zip_list_1 = ['박','성']
zip_list_2 = ['현']
print(list(zip(zip_list_1, zip_list_2))) # [('박','현')]
zip_list_3 = ['박','성','현']
zip_list_4 = ['park','seong','hyun']
print(list(zip(zip_list_3,zip_list_4))) # [('박', 'park'), ('성', 'seong'), ('현', 'hyun')]

for zip_list_3,zip_list_4 in zip(zip_list_3, zip_list_4):
    print(zip_list_3, zip_list_4) # 박 park
                                  # 성 seong
                                  # 현 hyun

#list(map(int, input().split())) : 입력 받은 숫자를 list로 바꿔줌
nums = list(map(int, input().split()))
print(nums) # I : 345
            # O : [345]