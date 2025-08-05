
'''

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
'''
from token import tok_name

from direct.showbase.PythonUtil import printNumberedTyped


# wysokosc = 5
# liczba = 0
# for wiersz in range(wysokosc):
#     for kolumna in range(2 * wysokosc - 1):
#         if kolumna >= wysokosc - wiersz - 1 and kolumna <= wysokosc + wiersz -1:
#
#
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

class Solution:
    def isPowerOfTwo(n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

    print(isPowerOfTwo(3))

