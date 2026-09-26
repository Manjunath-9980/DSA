class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        data = dict(knowledge)
        result = ""
        i = 0

        while i < len(s):
            if s[i] == "(":
                key = ""
                i += 1

                while s[i] != ")":
                    key += s[i]
                    i += 1

                result += data.get(key, "?")
            else:
                result += s[i]

            i += 1

        return result