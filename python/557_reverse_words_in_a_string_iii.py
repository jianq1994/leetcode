class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for num in range(len(words)):
            words[num] = words[num][::-1]
        return " ".join(words)