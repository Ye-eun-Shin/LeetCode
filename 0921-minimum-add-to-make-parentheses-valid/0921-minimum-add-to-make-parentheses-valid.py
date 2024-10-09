class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        - 괄호 짝을 맞출 것 : ( -> ) 순서만 가능
        - 스택 사용 : 짝이 되면 같이 스택에서 pop됨.
        """
        if len(s)==0:
            return 0

        stack = []
        stack.append(s[0])

        for i in range(1, len(s)):
            if len(stack)==0:
                stack.append(s[i])
                continue
            if stack[-1]=='(' and s[i]==')':
                stack.pop(-1)
            else:
                stack.append(s[i])
        
        return len(stack)
