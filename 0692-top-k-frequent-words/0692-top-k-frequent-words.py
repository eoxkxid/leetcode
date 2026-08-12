class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 1. 각 단어의 등장 빈도 계산
        frequency = Counter(words)

        # 빈도수의 최대값은 len(words)
        buckets = [[] for _ in range(len(words) + 1)]

        # 2. 빈도수를 bucket의 index로 사용
        for word, count in frequency.items():
            buckets[count].append(word)

        result = []

        # 3. 높은 빈도수부터 확인
        for count in range(len(words), 0, -1):

            # 같은 빈도에서는 사전순 정렬
            buckets[count].sort()

            for word in buckets[count]:
                result.append(word)

                # k개를 모두 찾았으면 종료
                if len(result) == k:
                    return result

        return result