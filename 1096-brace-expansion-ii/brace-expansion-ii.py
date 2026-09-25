class Solution:
    def braceExpansionII(self, expression):
        def parse(i):
            res = set()
            cur = {""}

            while i < len(expression) and expression[i] != "}":
                if expression[i] == "{":
                    part, i = parse(i + 1)
                    cur = {a + b for a in cur for b in part}
                elif expression[i] == ",":
                    res |= cur
                    cur = {""}
                    i += 1
                else:
                    cur = {a + expression[i] for a in cur}
                    i += 1

            res |= cur
            return res, i + 1

        return sorted(parse(0)[0])