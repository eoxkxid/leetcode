class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 1. 각 단어의 등장 횟수 계산
        frequency = Counter(words)

        # 2. 빈도수 내림차순,
        #    빈도가 같으면 사전순 오름차순으로 정렬
        sorted_words = sorted(
            frequency.keys(),
            key=lambda word: (-frequency[word], word)
        )

        # 3. 앞에서 k개 반환
        return sorted_words[:k]