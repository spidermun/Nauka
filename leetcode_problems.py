# from typing import List
#
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)
#         y = x_str[::-1]
#         print(x)
#         return x_str == y
#
# class Solution1:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         p = strs[0]
#         for s in strs[1:]:
#             while not s.startswith(p):
#                 p = p[:-1]
#                 if not p:
#                     return ""
#         return p
#
# class Solution2:
#     def sum(self, num1: int, num2: int) -> int:
#         num3 = num1 + num2
#         return num3
#
#
#
#
#
# '''
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
#
#
#
# Example 1:
#
#     Input: nums = [1,2,3,4]
#     Output: [1,3,6,10]
#     Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
#
#     Input: nums = [1,1,1,1,1]
#     Output: [1,2,3,4,5]
#     Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
#
# Example 3:
#
#     Input: nums = [3,1,2,10,1]
#     Output: [3,4,6,16,17]
# '''
#
# class Solution3:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         liczby = []
#         suma = 0
#         for num in nums:
#             suma += num
#             liczby.append(suma)
#         return liczby
#
# class Solution4:
#     def numberOfSteps(self, num: int) -> int:
#         kroki = 0
#         while num > 0:
#             if num % 2 == 0:
#                 num /= 2
#                 kroki += 1
#             else:
#                 num -= 1
#                 kroki += 1
#         return kroki
#
#
# class Solution5:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         wartosc = 0
#         for account in accounts:
#             o_w = sum(account)
#             if o_w > wartosc:
#                 wartosc = o_w
#         return wartosc
#
#
#
#
# class Solution6:
#     def kidsWithCandies(self, candies, extraCandies):  # dodaj 'self'
#         # Znajdź maksymalną liczbę cukierków, jaką ma któreś dziecko
#         max_candies = max(candies)
#
#         # Stwórz pustą listę na wyniki (True lub False)
#         result = []
#
#         # Przejdź przez każde dziecko (czyli przez każdy element listy candies)
#         for candy in candies:
#             # Dodaj extraCandies do aktualnego dziecka
#             total = candy + extraCandies
#
#             # Sprawdź, czy po dodaniu ma najwięcej lub tyle samo co max
#             if total >= max_candies:
#                 result.append(True)
#             else:
#                 result.append(False)
#
#         # Zwróć listę wyników
#         return result
#
#
# print(Solution6().kidsWithCandies([2,3,5,1,3], 3))  # poprawne wywołanie


class Solution:
    def romanToInt(self, s: str) -> int:









