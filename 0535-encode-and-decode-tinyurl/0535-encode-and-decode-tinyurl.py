class Codec:
    def __init__(self):
        # 짧은 URL의 공통 앞부분
        self.base_url = "http://tinyurl.com/"

        # shortUrl -> longUrl
        # decode할 때 사용
        self.short_to_long = {}

        # longUrl -> shortUrl
        # 같은 longUrl이 다시 들어왔는지 확인할 때 사용
        self.long_to_short = {}

        # 새로운 shortUrl 번호를 만들기 위한 카운터
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """
        긴 URL을 짧은 URL로 인코딩한다.
        """
        # 이미 인코딩한 긴 URL이면 기존 shortUrl을 그대로 반환
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]

        # 처음 보는 긴 URL이면 새로운 shortUrl 생성
        shortUrl = self.base_url + str(self.counter)

        # 다음 URL을 위해 counter 증가
        self.counter += 1

        # 양방향 매핑 저장
        self.short_to_long[shortUrl] = longUrl
        self.long_to_short[longUrl] = shortUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """
        짧은 URL을 원래 URL로 디코딩한다.
        """
        return self.short_to_long[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))