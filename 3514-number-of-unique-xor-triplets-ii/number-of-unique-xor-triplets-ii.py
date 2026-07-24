class Solution:

    def uniqueXorTriplets(self, nums: list[int]) -> int:

        unique_nums = list(set(nums))

        max_val = max(unique_nums)
        limit = 1
        while limit <= max_val:
            limit <<= 1

        has_pair = [False] * limit
        n_unique = len(unique_nums)

        for i in range(n_unique):
            x = unique_nums[i]
            for j in range(i, n_unique):
                y = unique_nums[j]
                has_pair[x ^ y] = True

        pairs = [p for p in range(limit) if has_pair[p]]

        has_triplet = [False] * limit
        for p in pairs:
            for x in unique_nums:
                has_triplet[p ^ x] = True

        return sum(has_triplet)