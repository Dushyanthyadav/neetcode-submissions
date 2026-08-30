class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recursive(op, cl, arr):
            if op == cl == n:
                res.append(''.join(arr))
                return

            if op < n:
                arr.append('(')
                recursive(op + 1, cl, arr)
                arr.pop()

            if cl < op:
                arr.append(')')
                recursive(op, cl + 1, arr)
                arr.pop()

        recursive(0, 0, [])
        return res

        