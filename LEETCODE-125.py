class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = "".join(i for i in s1 if i.isalnum())
        if ( s2 == s2[::-1]):
            return True
        else:
            return False 