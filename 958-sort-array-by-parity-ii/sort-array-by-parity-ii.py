class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = 1

        while i < n and j < n:
            if nums[i] %2  == 0:
                i = i+2
            elif nums[j]%2 == 1:
                j = j+2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
