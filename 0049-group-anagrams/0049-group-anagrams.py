class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            # 애너그램은 정렬하면 같은 문자열이 된다.
            key = ''.join(sorted(word))
            anagram_groups[key].append(word)

        return list(anagram_groups.values())