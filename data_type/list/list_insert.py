'''
* 리스트에 데이터를 추가하는 메서드

1. append(): 요소를 리스트의 맨 마지막에 추가.
2. insert(): 요소를 리스트의 특정 위치에 삽입.
'''
nums = [1,3,5,7]

nums.append(9)
print(nums)

nums.append('하이')
print(nums)

# insert(인덱스, 추가하고자하는값) 
nums.insert(1, 2)
print(nums)
