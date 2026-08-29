class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        sorted_nums = sorted(nums)
        groups = []
        current_group = [sorted_nums[0]]

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] <= limit:
                current_group.append(sorted_nums[i])
            else:
                groups.append(current_group)
                current_group = [sorted_nums[i]]

        groups.append(current_group)

        value_to_group = {}
        for group_id, group in enumerate(groups):
            for value in group:
                value_to_group.setdefault(value, []).append(group_id)

        group_indices = [[] for _ in groups]

        for i, value in enumerate(nums):
            group_id = value_to_group[value].pop()
            group_indices[group_id].append(i)

        answer = nums[:]

        for group_id, indices in enumerate(group_indices):
            values = groups[group_id]
            indices.sort()

            for index, value in zip(indices, values):
                answer[index] = value

        return answer