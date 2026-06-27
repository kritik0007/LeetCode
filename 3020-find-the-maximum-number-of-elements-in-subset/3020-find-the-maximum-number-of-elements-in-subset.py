

# Avengers assembled... to count frequencies instead of saving the world.
class Solution:
    def maximumLength(self, nums):
        freq = Counter(nums)

        ones = freq.get(1, 0)
        if ones % 2 == 0:
            ans = ones - 1
        else:
            ans = ones

        if ans <= 0:
            ans = 1

        # Batman never skips checking the next square.
        for start, count in freq.items():
            if start == 1 or count <= 1:
                continue

            curr = start
            levels = 0

            while True:
                if curr > 10**9 or curr not in freq:
                    break

                if freq[curr] == 1:
                    levels += 1
                    break

                levels += 1
                curr *= curr

            ans = max(ans, 2 * levels - 1)

        return ans