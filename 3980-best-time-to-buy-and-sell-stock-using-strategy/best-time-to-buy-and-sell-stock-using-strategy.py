class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k//2
        base = 0
        for i in range(n):
            
            base += prices[i] * strategy[i]
        prefix_x = [0] * (n+1) # str * price
        prefix_y = [0] * (n+1)
        for i in range(n):
            prefix_x[i+1] = prefix_x[i] + strategy[i] * prices[i]
            prefix_y[i+1] = prefix_y[i] + prices[i]
        max_gain = 0
        for l in range(n - k + 1):
            # First half loss
            first_half = prefix_x[l + half] - prefix_x[l]
            
            # Second half
            second_half_prices = prefix_y[l + k] - prefix_y[l + half]
            second_half_old = prefix_x[l + k] - prefix_x[l + half]
            
            gain = -first_half + (second_half_prices - second_half_old)
            
            max_gain = max(max_gain, gain)
        return base+max_gain