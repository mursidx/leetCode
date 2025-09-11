class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


solution = Solution()


print(solution.isPalindrome(121)) 
print(solution.isPalindrome(123)) 