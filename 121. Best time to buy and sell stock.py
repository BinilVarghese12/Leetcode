class Solution(object):
    def maxProfit(self, prices):
        cheapest = prices[0]
        max_profit = 0

        for x in range(len(prices)):
            current = prices[x]

            if current < cheapest:
                cheapest = current
            profit = current - cheapest

            if profit > max_profit:
                max_profit = profit
        return max_profit

        