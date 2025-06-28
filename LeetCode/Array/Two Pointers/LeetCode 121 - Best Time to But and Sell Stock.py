# LeetCode 121 : Best Time to Buy and Sell Stock
# Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    buy = 0  # Pointer 1
    sell = 1  # Pointer 2
    max_profit = 0  # Variable to store the maximum profit encountered

    while sell < len(prices):  # Iterate till sell pointer reaches the end of list
        if prices[buy] < prices[sell]:  # Check if the current buy-price is less than the current sell-price
            profit = prices[sell] - prices[buy]  # If yes, calculate profit
            if profit > max_profit:  # Update max_profit, if the current profit is greater
                max_profit = profit
        else:  # Instead, if current buy-price is more than sell-price, update buy pointer,
            buy = sell # so that we can buy at the lowest available price.
        sell += 1  # Increment sell pointer to check for the next profit margin

    return max_profit  # Return the maximum profit found


# Test case: Example array of stock prices
price1 = [2,1,5,3,4,6]
profit1 = maxProfit(price1)
print(profit1)  # Output = 5
