import random, string

class Codec:
    def __init__(self):
        self.dic = {}
        self.shorturl = 'http://tinyurl.com/'
        self.S = string.ascii_lowercase+string.ascii_uppercase+string.digits

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        x = ''.join(random.choice(self.S) for _ in range(4))
        self.dic[x] = longUrl
        return self.shorturl+x
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        x = shortUrl.replace(self.shorturl,'')
        return self.dic[x]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))