### 2) Given a positive integer num, return true if num is a perfect square or false otherwise.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return ((num)**0.5)%1 == 0
