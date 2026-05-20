stock_prices = {
    "AAPL": 150.25,
    "TSLA": 720.50,
    "GOOGL": 2800.75,
    "MSFT": 320.60
}
total_investment = 0
stock_name = input("Enter stock name: ")
quantity = int(input("Enter quantity: "))
if stock_name in stock_prices:
    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment
    
    print(f"Current price of {stock_name}: ${price:.2f}")
    print(f"Total value: ${total_investment:.2f}")
    print(f"Total investment is: ${total_investment:.2f}")
else:
    print(f"stock ticker '{stock_name}' not found.")
  
