# LeetCode 121 : Best Time to Buy and Sell Stock
# Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    buy_price = 0  # Pointer 1
    sell_price = 1  # Pointer 2
    max_profit = 0  # Variable to store the maximum profit encountered

    while sell_price < len(prices):  # Iterate till sell pointer reaches the end of list
        if prices[sell_price] > prices[buy_price]:  # Check if the current sell_price is greater than the buy-price
            profit = prices[sell_price] - prices[buy_price]  # If yes, calculate current profit
            if profit > max_profit:  # Update max_profit, if the current profit is greater
                max_profit = profit

        else:  # Instead, if sell_price is lower than the buy-price, update buy pointer,
            buy_price = sell_price  # so that we can buy at the lower price that is available.

        sell_price += 1  # Increment sell pointer to check for the next profit margin / buying opportunity

    return max_profit  # Return the maximum profit found


# Test case: Example array of stock prices
price1 = [2,1,5,3,8,6]
profit1 = maxProfit(price1)
print(profit1)  # Output = 7
