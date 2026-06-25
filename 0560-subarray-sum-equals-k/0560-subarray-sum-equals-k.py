class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)

        # 누적합 0이 처음에 한 번 있었다고 처리
        # 그래야 index 0부터 시작하는 부분 배열도 세어진다
        prefix_count[0] = 1

        prefix_sum = 0
        answer = 0

        for num in nums:
            prefix_sum += num

            # 현재 누적합에서 k를 뺀 값이 이전에 있었다면,
            # 그 개수만큼 합이 k인 부분 배열이 존재한다.
            needed_sum = prefix_sum - k
            answer += prefix_count[needed_sum]

            # 현재 누적합을 기록
            prefix_count[prefix_sum] += 1

        return answer