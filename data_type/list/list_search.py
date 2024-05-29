'''
* 리스트의 탐색과 정렬

1. index(): 리스트에서 특정 값이 저장된 인덱스를 반환.
2. count(): 리스트 내부에 저장된 특정 요소의 개수를 반환.
3. sort(): 리스트를 오름차 정렬.
4. reverse(): 리스트 데이터를 역순으로 배치
'''
points = [44, 84, 23, 100, 75, 100, 22]
perfect = points.count(100)
print(f'100점을 획득한 학생은 {perfect}명입니다.')

print(f'44점을 획득한 학생은 {points.index(44)+1}번째 학생입니다.')

# 내장함수 len(), max(), min()
print(f'학생 수는 {len(points)}명 입니다.')
print(f'최고 점수는 {max(points)} 입니다')
print(f'최저 점수는 {min(points)} 입니다')

# 오름차 정렬 sort()
print('-' * 40)

print(points)
# points.sort() 오름차
points.sort(reverse=True) # 내림차
# points.reverse() # 역순
# (내림차 : 오름차 -> 역순)
print(points)

# 리스트 내의 요소의 단순 존재 유무를 확인 하려면 in 키워드를 사용합니다.
food_menu = ['김밥', '닭강정', '라면', '밥말리']
name = input('음식명을 입력하세요: ')

if name in food_menu:
    print(f'{name}은 food_menu에 포함되어있습니다.')
    print('주문완료!')
else:
    print('주문할 수 없습니다.')
