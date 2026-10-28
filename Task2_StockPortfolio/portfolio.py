
import csv

portfolio = {
    "AAPL": {"buy_price": 150.00, "quantity": 5, "current_price": 175.00},
    "MSFT": {"buy_price": 300.00, "quantity": 2, "current_price": 350.00},
    "GOOGL": {"buy_price": 140.00, "quantity": 3, "current_price": 160.00}
}

# Load company tickers from the S&P 500 dataset
with open("constituents.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    valid_tickers = {row["Symbol"].strip() for row in reader}

total_investment = 0
total_current_value = 0

print("\n===== STOCK PORTFOLIO TRACKER =====")
print("Note: Current prices are sample values, not live prices.\n")

with open("portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Ticker", "Buy Price", "Quantity", "Sample Current Price",
        "Investment", "Current Value", "Profit/Loss", "Gain/Loss (%)"
    ])

    for ticker, details in portfolio.items():
        if ticker not in valid_tickers:
            print(f"Warning: {ticker} was not found in the S&P 500 dataset.")
            continue

        buy_price = details["buy_price"]
        quantity = details["quantity"]
        current_price = details["current_price"]

        investment = buy_price * quantity
        current_value = current_price * quantity
        profit_loss = current_value - investment
        percentage = (profit_loss / investment) * 100

        total_investment += investment
        total_current_value += current_value

        print(f"\nStock: {ticker}")
        print(f"Investment: {investment:.2f}")
        print(f"Current value: {current_value:.2f}")
        print(f"Profit/Loss: {profit_loss:.2f}")
        print(f"Gain/Loss: {percentage:.2f}%")

        writer.writerow([
            ticker, buy_price, quantity, current_price,
            round(investment, 2), round(current_value, 2),
            round(profit_loss, 2), round(percentage, 2)
        ])

    total_profit_loss = total_current_value - total_investment
    total_percentage = (
        (total_profit_loss / total_investment) * 100
        if total_investment else 0
    )

    print("\n===== PORTFOLIO SUMMARY =====")
    print(f"Total investment: {total_investment:.2f}")
    print(f"Total current value: {total_current_value:.2f}")
    print(f"Total profit/loss: {total_profit_loss:.2f}")
    print(f"Overall change: {total_percentage:.2f}%")

    writer.writerow([])
    writer.writerow([
        "TOTAL", "", "", "", round(total_investment, 2),
        round(total_current_value, 2),
        round(total_profit_loss, 2), round(total_percentage, 2)
    ])

print("\nReport saved to portfolio_summary.csv")
