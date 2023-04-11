# A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters
# include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            while not self.alphaNum(s[left]):
                left += 1
            while not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True

    # own alpha-numeric function

    def alphaNum(self, char):
        return (
            ord("A") <= ord(char) <= ord("Z")
            or ord("a") <= ord(char) <= ord("z")
            or ord("0") <= ord(char) <= ord("9")
        )

        # word = ""
        # for char in s:
        #     if char.isalpha():
        #         lower_char = char.lower()
        #         word += lower_char
        # reverse_word = word[::-1]
        # if word == reverse_word:
        #     return True
        # return False
