class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)
        if length%2==1: # 길이가 홀수면 짝이 안 맞으므로 불가능
            return False
        
        open_brackets = [] # to stack '(' in the locked positions
        unlocked = [] # 바뀔 수 있는 것 index 저장
        for i in range(length):
            if locked[i]=='0':
                unlocked.append(i)
            else:
                if s[i]=='(':
                    open_brackets.append(i)
                else:
                    if open_brackets:
                        open_brackets.pop()
                    elif unlocked:
                        unlocked.pop()
                    else:
                        return False

        while unlocked and open_brackets:
            o = open_brackets.pop()
            u = unlocked.pop()
            if o>u:
                return False
        
        if open_brackets:
            return False
        return True