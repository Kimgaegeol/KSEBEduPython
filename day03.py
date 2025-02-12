import math

def my_pow(b, e) -> float:
    """

    :param b:
    :param e:
    :return:
    """

    result = 1

    if e == 0:
        pass
    elif e > 0:

        i = int(e)
        f = e - i

        for _ in range(i):
            result = result * b


        if f > 0:
            result = result * math.exp(f * math.log(b))

    else:
        i = int(-e)
        f = -e -  i

        for _ in range(i):
            result = result * b


        if f > 0:
            result =result * math.exp(f * math.log(b))

        result =  1/ result

    return result

# print(my_pow(2,-1))

# 1. fork 떠서 가져가기
# 2. 로컬에 clone
# 3. branch 파기
# 4. switch(checkout)
# 5. day2 소스코드 수정
# 6. add commit push (git push -u origin '내가만든branch')
# 7. pull request
# 8. branch -d
# 9. 원본 리포지토리 clone

#===============================================================================================================================

# subjects = ["데이터베이스", "C++", "5", "Java", "Python", "Java", "9", "리눅스"]
# print(subjects[::-1])
# subjects[::-1]
# subjects = subjects[::-1]  # subjects.reverse()
# print(subjects)
# subjects.remove("Java")
# del subjects[-2]
#del subjects[2]
# print(subjects.pop(1))
# subjects.sort()  # desc
# subjects.sort(reverse=True)  # desc
# copy_subjects = sorted(subjects)
# print(subjects)
# print(copy_subjects)

#===============================================================================================================================

# import copy
# # subjects = ["a", "b", "c"]
# subjects = ["a", ["b", "c"], "d"]
# a = subjects # 얘는 서로 바뀌면 서로 바뀜
# b = subjects.copy() # 여기서부터는 카피한 것
# c = list(subjects)
# d = subjects[:]
# e = copy.deepcopy(a)
#
# print(subjects, a, b, c, d, e)
#
# subjects[1][1] = "x"
#
# print(subjects)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e) # 얘만 자기 공간을 할당받았다는 것을 알 수 있음

#===============================================================================================================================

# squares = list()
# squares.append(1*1)
# squares.append(2*2)
# squares.append(3*3)
# squares.append(4*4)
# squares.append(5*5)
# print(squares)

# squares = list()
# for i in range(1, 6, 1):
#     squares.append(i*i)
# print(squares)

# list comprehension
# squares = [i*i for i in range(1, 6, 1)]
# print(squares)

# even_squares = [i*i for i in range(1, 6, 1) if i % 2 == 0]
# print(even_squares)

#===============================================================================================================================

# sugang = dict(python="kim", cpp="sung", db="kang")
# print(sugang)
# sugang['datastructure'] = 'kim'  # add
# print(sugang)
# sugang['datastructure'] = 'park'  # update
# print(sugang)
# print(sugang['db'])
# print(sugang.get('db'))
# print(sugang.get('opensource'))
# print(sugang.get('opensource', 'not exist'))
# for subject, professor in sugang.items():
#     print(f'{subject} 과목 담당교수는 {professor}입니다')

# for k in sugang.keys():
# for k in sugang:
#     print(k)

# for v in sugang.values():
#     print(v)

# for s in sugang.items():
#     print(s)

#===============================================================================================================================

# drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
#
# # drink = input(drinks_foods.keys())
# drinks_foods_keys = list(drinks_foods)
# # print(drinks_foods_keys)
#
# while True:
#     menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) 종료 : ')
#     if menu == '1':
#         print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
#     elif menu == '2':
#         print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
#     elif menu == '3':
#         print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
#     elif menu == '4':
#         print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
#     elif menu == '5':
#         print(f'다음에 또 오세요')
#         break

# ===============================================================================================================================

# import random

# drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
# # print(drinks_foods)
# # print(drinks_foods.pop("고량주"))
# # print(drinks_foods)
#
# del drinks_foods["위스키"]
# drinks_foods["사케"] = "광어회"
# japan_drinks_foods = {"사케": "광어회", "위스키": "낙곱새"}
# drinks_foods.update(japan_drinks_foods)
# print(drinks_foods)
#
# #drink = input(drinks_foods.keys())
# drinks_foods_keys = list(drinks_foods)
# # print(drinks_foods_keys)
# # #print(drinks_foods_keys.pop(0))
# # print(drinks_foods_keys.remove("위스키"))
# # print(drinks_foods_keys)
# print(random.choice(drinks_foods_keys))
#
# while True:
#     menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) {drinks_foods_keys[4]}   6) 아무거나   7) 종료 : ')
#     if menu == '1':
#         print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
#     elif menu == '2':
#         print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
#     elif menu == '3':
#         print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
#     elif menu == '4':
#         print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
#     elif menu == '5':
#         print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]} 입니다')
#     elif menu == '6':
#         random_drink = random.choice(drinks_foods_keys)
#         print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')
#     elif menu == '7':
#         print(f'다음에 또 오세요')
#         break

# star = ['태란', ' 저그', '프로토스']
# print(random.choice(star))
# # print(random.randint(1,6))
# print(star[random.randint(0,2)])

# ===============================================================================================================================

# Assignment ex 8.10
# squares = {n: pow(n, 2) for n in range(10)}
#squares = {n: n**2 for n in range(10)}
# squares = {n: n*n for n in range(10)}
# print(squares)

# univ = 'inha university'
# counts_alphabet = {letter: univ.count(letter) for letter in univ}  # dictionary comprehension
# print(counts_alphabet)

# univ = 'inha university'
# counts_alphabet = dict()
# for letter in univ:
#     counts_alphabet[letter] = univ.count(letter)
# print(counts_alphabet)

# ===============================================================================================================================

# v4.3까지 했음