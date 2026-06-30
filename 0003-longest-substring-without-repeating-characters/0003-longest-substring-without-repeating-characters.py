class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # 현재 문자가 윈도우 안에서 이미 등장했다면 left를 이동
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            # 현재 문자의 마지막 등장 위치 갱신
            last_seen[char] = right

            # 현재 윈도우 길이 계산
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length