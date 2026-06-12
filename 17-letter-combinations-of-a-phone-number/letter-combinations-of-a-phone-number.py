class Solution:
    def letterCombinations(self, digits: str):

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = [""]

        for digit in digits:

            temp = []

            for current in result:

                for ch in phone[digit]:
                    temp.append(current + ch)

            result = temp

        return result