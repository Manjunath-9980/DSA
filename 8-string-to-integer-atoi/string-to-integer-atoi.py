class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        number = 0

        # Ignore spaces at the beginning
        while i < len(s) and s[i] == " ":
            i += 1

        # Check the sign
        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1

        # Read the digits
        while i < len(s) and s[i] >= "0" and s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            number = number * 10 + digit
            i += 1

        number = number * sign

        # Keep the number inside 32-bit integer range
        if number < -2**31:
            return -2**31

        if number > 2**31 - 1:
            return 2**31 - 1

        return number