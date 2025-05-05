#문자열 관련

#str.split() : 공백 기준으로 나눠줌
#str.split(",") 인자로 넣은 문자를 기준으로 나눠줌
#string -> list로 변함
str_split = "박성현,박성현"
print(str_split.split(",")) # ['박성현','박성현']

#'구분자'.join(list)
str_join = ''.join(str_split)
print(str_join) # 박성현,박성현

#str.strip() : 양쪽 공백 제거 , 인자 입력시 양쪽 입력된 인자 제거
#str.rstrip() : 우측 공백 제거 , 인자 입력시 우측 입력된 인자 제거
#str.lstrip() : 좌측 공백 제거 , 인자 입력시 좌측 입력된 인자 제거
str_strip = "##박성현##"
print(str_strip) # ##박성현##
print(str_strip.strip('#')) # 박성현
print(str_strip.rstrip('#')) # ##박성현
print(str_strip.lstrip('#')) # 박성현##

#str.replace(old,new) : 기존 문자 , 바꿀 문자
str_replace = "박성현"
print(str_replace.replace('박','김')) # 김성현

#str.find(찾을 문자) : 찾을 문자(열) 가 있는 먼저 발견된 시작 인덱스 알려줌
#찾는 문자가 발견 되지 않으면 -1 반환
str_find = "박성현현성현"
print(str_find.find('성현')) # 2

#str.index(찾을 문자) : 마찬가지로 먼저 발견된 시작 인덱스 알려줌
#찾는 문자가 발견 되지 않으면 에러남
str_index = '박성현박'
print(str_index.index("현박")) # 2

#str.count(개수가 궁금한 문자(열)) : 몇개가 있는지 알려줌
str_count = "박성성성성성현현현현"
print(str_count.count("성현")) # 1

#str.isdigit : 문자열이 전부 숫자면 진실
#str.isalpha : 문자열이 전부 문자면 진실
#str.isalnum : 문자열이 전부 문자 또는 숫자면 진실
str_isdigit = "12345"
str_isalpha = "Park성현"
str_isalnum = "Park성현123"
print(str_isdigit.isdigit()) # True
print(str_isalpha.isalpha()) # True
print(str_isalnum.isalnum()) # True

#str.upper : 소문자를 대문자로 변경
#str.lower : 대문자를 소문자로 변경
str_upper = "abcd"
str_lower = "ABCD"
print(str_upper.upper()) # ABCD
print(str_lower.lower()) # abcd

#str[::-1] : 문자열 뒤집기
str_reverse = "현성박"
print(str_reverse[::-1]) # 박성현

