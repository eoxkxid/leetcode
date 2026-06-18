class Codec:
    def __init__(self):
        self.base_url = "http://tinyurl.com/"
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        self.long_to_code = {}
        self.code_to_long = {}
        self.counter = 0

    def _to_base62(self, num: int) -> str:
        # 0도 유효한 코드로 처리
        if num == 0:
            return self.chars[0]

        code = []

        while num > 0:
            remainder = num % 62
            code.append(self.chars[remainder])
            num //= 62

        # 나머지부터 구했기 때문에 뒤집어야 정상적인 Base62 표현이 된다
        return ''.join(reversed(code))

    def encode(self, longUrl: str) -> str:
        """
        긴 URL을 짧은 URL로 인코딩한다.
        """
        # 이미 인코딩한 URL이면 기존 코드를 재사용
        if longUrl in self.long_to_code:
            code = self.long_to_code[longUrl]
            return self.base_url + code

        # 새로운 URL이면 새로운 코드 생성
        code = self._to_base62(self.counter)
        self.counter += 1

        self.long_to_code[longUrl] = code
        self.code_to_long[code] = longUrl

        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        """
        짧은 URL을 원래 URL로 디코딩한다.
        """
        code = shortUrl.split("/")[-1]
        return self.code_to_long[code]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))