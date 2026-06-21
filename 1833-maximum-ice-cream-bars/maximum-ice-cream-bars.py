class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        max_c = max(costs)
        freq = [0] * (max_c + 1)
        
        for c in costs:
            freq[c] += 1
            
        count = 0
        for price in range(1, max_c + 1):
            if freq[price] > 0:
                num_to_buy = min(freq[price], coins // price)
                
                count += num_to_buy
                coins -= num_to_buy * price
                
                if coins < price:
                    break
                    
        return count