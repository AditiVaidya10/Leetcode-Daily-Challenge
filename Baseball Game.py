class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for i in ops:
            if i.isdigit():
                arr.append(int(i))
            elif i == 'C':
                arr.pop()
            elif i == 'D':
                arr.append(arr[-1] * 2)
            elif i == '+':
                arr.append(arr[-1] + arr[-2])
            else:
                arr.append(int(i))
        return sum(arr)
