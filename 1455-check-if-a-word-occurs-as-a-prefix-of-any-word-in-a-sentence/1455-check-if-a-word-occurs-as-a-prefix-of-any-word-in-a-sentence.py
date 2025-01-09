class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        lens = len(searchWord)
        answer = -1
        for i, w in enumerate(words):
            if len(w)<lens:
                continue
            if w[:lens]==searchWord:
                answer = i+1
                break
                
        return answer