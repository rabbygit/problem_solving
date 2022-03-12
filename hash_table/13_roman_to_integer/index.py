class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        num = 0
        length = len(s)
        i = 0

        while(i <= length-1):
            if i+1 <= length-1 and s[i] + s[i+1] in roman_num:
                num += roman_num[s[i]+s[i+1]]
                i += 1
            else:
                num += roman_num[s[i]]

            i += 1

        return num