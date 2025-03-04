class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 마지막 숫자가 9가 아닐 때까지 업데이트
        # 9 앞에 숫자가 있는 경우, 없는 경우.
        # 9가 아닌 경우 while 문 나가서 해당 자리 +1
        i = len(digits)-1
        while digits[i]==9:
            digits[i]=0
            if not i:
                digits.insert(0, 0)
                break
            i-=1
        digits[i]+=1
        return digits