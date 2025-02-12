class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
           return 0  # 빈 배열 처리

        i = 0  # 고유한 원소를 저장할 위치

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # 새로운 고유 원소 발견
                i += 1  # 위치 이동
                nums[i] = nums[j]  # 새로운 값 저장

        return i + 1  # 고유 원소 개수 반환

'''
투 포인터(two-pointer)
1. 입력 배열이 정렬되어 있기 때문에, 중복된 값들은 연속해서 등장.
2. 두 개의 포인터 사용
    - i: 중복되지 않은 고유 원소를 저장할 위치
    - j: 배열을 탐색하면서 중복되지 않은 원소를 찾는 역할
3. 반복문을 통해 배열을 탐색하면서 중복 제거
4. 최종적으로 i+1이 고유한 원소의 개수 
'''