class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 채점을 nums 전체에 대해서 동일한지 보는 게 아니라 딱 정답 길이만큼만 탐색하기 때문에
        # 정답 길이 이후에 요소가 있어도 상관이 없다.
        # => 투 포인터를 써서, 앞에랑 같지 않을 때만 차례대로 덮어씌워주면 된다.
        # 아래의 코드는 내 코드고 위의 내용과는 같지 않다...
        # pop을 해주었더니 효율이 극악이 됐다
        prev = nums[0]
        length = len(nums)
        i=1
        while i<length:
            if nums[i]==prev:
                nums.pop(i)
                length-=1
            else:
                prev = nums[i]
                i+=1
        return length