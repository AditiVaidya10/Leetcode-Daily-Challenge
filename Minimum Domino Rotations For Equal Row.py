class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tops_len = len(tops)

        frequency_tops = Counter(tops)
        frequency_bottoms = Counter(bottoms)

        swap_number = None

        for i in range(1,7):
            if frequency_tops[i] + frequency_bottoms[i] >= tops_len:
                swap_number = i
                break

        if swap_number is None:
            return -1

        for i in range(tops_len):
            if swap_number not in [tops[i],bottoms[i]]:
                return -1

        min_num1 = tops_len-frequency_tops[swap_number]
        min_num2 = len(bottoms)-frequency_bottoms[swap_number]

        return min(min_num1,min_num2)
