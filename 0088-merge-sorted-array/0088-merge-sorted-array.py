class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 투 포인터 권법 사용
        i = 0 # nums1 안에서 돌기
        j = 0 # nums2 안에서 돌기

        while i<m and j<n:
            if nums1[i]>=nums2[j]:
                nums1.insert(i, nums2[j])
                i+=1
                j+=1
                m+=1 # 전체 요소 개수 업데이트
            
            else:
                i+=1
        
        if j<n:
            while j<n:
                nums1.insert(i, nums2[j])
                i+=1
                j+=1
                m+=1
        
        while len(nums1)>m:
            nums1.pop()