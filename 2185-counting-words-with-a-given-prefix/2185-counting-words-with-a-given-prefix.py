class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_len = len(pref)
        cnt = 0
        for w in words:
            if w[:pref_len]==pref:
                cnt+=1
        
        return cnt