class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        for i in range(n - k - 1, -1, -1):
            energy[i] = energy[i] + energy[i + k]

        max_path_energy = energy[0]
        for i in range(1, n):
            if energy[i] > max_path_energy:
                max_path_energy = energy[i]
                
        return max_path_energy