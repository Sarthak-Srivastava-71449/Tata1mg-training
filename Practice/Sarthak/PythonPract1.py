#This is the solution to the "Power of Two" problem in Leetcode which I earlier solved using C++
#Question link "https://leetcode.com/problems/power-of-two/"
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
         for i in range(31):
            ans = 2 ** i
            if ans == n:
                return True
         return False
    

#Solution to the "Reverse Integer" question from Leetcode in Python
#Question link "https://leetcode.com/problems/reverse-integer/"
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        ans = 0
        while x!= 0:
            dig = x%10
            if ans > (2147483647 // 10) or ans < (-(2147483648) // 10):
                return 0

            ans = (ans*10) + dig
            x = x//10

        if is_negative:
            ans = -ans

        return ans
    
#Solution to "Truncate sentence" problem
#Question link "https://leetcode.com/problems/truncate-sentence/"
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space = 0
        i = 0
        n = len(s)
        re = ""
        
        while i != n:
            if s[i] == ' ':
                space += 1
                
            if space == k:
                break
            
            re += s[i]
            i += 1
        
        return re
    
#Solution to "Valid Anagram" problem
#Question link "https://leetcode.com/problems/valid-anagram/"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True

        return False
    
#Solution to "Find Numbers with Even Number of Digits" problem
#Question Link "https://leetcode.com/problems/find-numbers-with-even-number-of-digits/"
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            count = 0
            k = i

            while k!= 0:
                k //= 10
                count += 1

            if count % 2 == 0:
                ans += 1

        return ans
    
#Solution to the "Reverse String" problem
#Question Link "https://leetcode.com/problems/reverse-string/"
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

#Solution to the "Best Time to Buy and Sell Stock" problem
#Question Link "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        ans = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                ans = max(ans, profit)
            else:
                left = right
            right += 1

        return ans
    
#Solution to the "Ugly Number" problem
#Question Link "https://leetcode.com/problems/ugly-number/"
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False

        for p in [2, 3, 5]:
            while n%p == 0:
                n = n // p
        return n == 1
    
#Solution to the "Length of Last Word" problem
#Question Link "https://leetcode.com/problems/length-of-last-word"
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        ans = 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            ans += 1
            i -= 1
        return ans