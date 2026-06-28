"""
CodeAlpha Python Internship - Task 2
Stock Portfolio Tracker

A simple stock tracker that calculates total investment based on
manually defined stock prices. Users input stock names and quantities,
and the program displays total investment and saves it to a file.

Author: Anam Shaheen
"""

# Hardcoded dictionary of stock prices (price per share in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

OUTPUT_FILE = "portfolio_summary.txt"


def show_available_stocks():
    """Display the list of stocks the user can invest in."""
    print("\nAvailable Stocks and Prices (per share):")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")


def get_user_portfolio():
    """Collect stock names and quantities from the user."""
    portfolio = {}

    print("\nEnter the stocks you want to add to your portfolio.")
    print("Type 'done' when you are finished.\n")

    while True:
        stock = input("Enter stock symbol (or 'done'): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found in our list. Please choose from the available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock} shares: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Add to portfolio (sum if stock already entered before)
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"Added {quantity} shares of {stock}.")

    return portfolio


def calculate_total_investment(portfolio):
    """Calculate the total investment value of the portfolio."""
    total = 0
    breakdown = {}

    for stock, quantity in portfolio.items():
        value = STOCK_PRICES[stock] * quantity
        breakdown[stock] = value
        total += value

    return total, breakdown


def save_to_file(portfolio, breakdown, total):
    """Save the portfolio summary to a text file."""
    with open(OUTPUT_FILE, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 30 + "\n")
        for stock, quantity in portfolio.items():
            f.write(f"{stock}: {quantity} shares x ${STOCK_PRICES[stock]} = ${breakdown[stock]}\n")
        f.write("=" * 30 + "\n")
        f.write(f"Total Investment: ${total}\n")


def main():
    print("=" * 40)
    print("Welcome to the Stock Portfolio Tracker")
    print("=" * 40)

    show_available_stocks()
    portfolio = get_user_portfolio()

    if not portfolio:
        print("\nNo stocks were added. Exiting.")
        return

    total, breakdown = calculate_total_investment(portfolio)

    print("\n" + "=" * 40)
    print("Portfolio Summary")
    print("=" * 40)
    for stock, quantity in portfolio.items():
        print(f"{stock}: {quantity} shares x ${STOCK_PRICES[stock]} = ${breakdown[stock]}")
    print("-" * 40)
    print(f"Total Investment: ${total}")
    print("=" * 40)

    save_choice = input("\nSave this summary to a file? (y/n): ").lower().strip()
    if save_choice == "y":
        save_to_file(portfolio, breakdown, total)
        print(f"Summary saved to {OUTPUT_FILE}")
    else:
        print("Summary not saved.")


if __name__ == "__main__":
    main()
