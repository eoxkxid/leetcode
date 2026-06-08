class MyHashMap:

    def __init__(self):
        # 소수를 사용하면 key 분포가 한쪽으로 몰릴 가능성을 줄일 수 있다.
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        # 이미 존재하는 key라면 value만 갱신
        for i, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                return

        # 존재하지 않는 ket라면 새로 추가한다.
        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]

        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value

        return -1        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)