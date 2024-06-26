# Exchange Rates are from 6/27/2024

exchange_rates = {
    "PHP": {"WON": 23.90, "YEN": 2.75, "EUR": 0.016, "USD": 0.020, "GBP": 0.014, "AUD": 0.029, "CAD": 0.027, "CHF": 0.018, "CNY": 0.13, "INR": 1.64, "PHP": 1},
    "WON": {"YEN": 0.12, "PHP": 0.041, "EUR": 0.00070, "USD": 0.00077, "GBP": 0.00060, "AUD": 0.0012, "CAD": 0.0011, "CHF": 0.00075, "CNY": 0.0055, "INR": 0.068, "WON": 1},
    "YEN": {"WON": 8.40, "PHP": 0.36, "EUR": 0.0061, "USD": 0.0071, "GBP": 0.0054, "AUD": 0.010, "CAD": 0.0096, "CHF": 0.0063, "CNY": 0.046, "INR": 0.57, "YEN": 1},
    "EUR": {"WON": 1440.50, "PHP": 62.50, "YEN": 162.50, "USD": 1.19, "GBP": 0.87, "AUD": 1.81, "CAD": 1.64, "CHF": 1.03, "CNY": 7.49, "INR": 93.65, "EUR": 1},
    "USD": {"WON": 48.30, "PHP": 48.00, "YEN": 129.00, "EUR": 0.84, "GBP": 0.71, "AUD": 1.52, "CAD": 1.37, "CHF": 0.86, "CNY": 6.31, "INR": 78.65, "USD": 1},
    "GBP": {"WON": 67.90, "PHP": 82.00, "YEN": 145.00, "EUR": 1.15, "USD": 1.41, "AUD": 2.14, "CAD": 1.93, "CHF": 1.23, "CNY": 8.90, "INR": 111.24, "GBP": 1},
    "AUD": {"WON": 32.50, "PHP": 34.80, "YEN": 98.00, "EUR": 0.55, "USD": 0.66, "GBP": 0.47, "CAD": 0.90, "CHF": 0.57, "CNY": 4.15, "INR": 51.58, "AUD": 1},
    "CAD": {"WON": 36.20, "PHP": 37.80, "YEN": 106.00, "EUR": 0.61, "USD": 0.73, "GBP": 0.52, "AUD": 1.11, "CHF": 0.63, "CNY": 4.63, "INR": 57.31, "CAD": 1},
    "CHF": {"WON": 57.40, "PHP": 41.30, "YEN": 160.00, "EUR": 0.97, "USD": 1.17, "GBP": 0.81, "AUD": 1.76, "CAD": 1.60, "CNY": 7.35, "INR": 91.32, "CHF": 1},
    "CNY": {"WON": 7.69, "PHP": 7.96, "YEN": 22.30, "EUR": 0.13, "USD": 0.16, "GBP": 0.11, "AUD": 0.24, "CAD": 0.22, "CHF": 0.14, "INR": 12.43, "CNY": 1},
    "INR": {"WON": 0.15, "PHP": 0.61, "YEN": 1.75, "EUR": 0.011, "USD": 0.013, "GBP": 0.009, "AUD": 0.019, "CAD": 0.018, "CHF": 0.011, "CNY": 0.080, "INR": 1}
}

currency_symbols = {"PHP": "₱", "WON": "₩", "YEN": "¥", "EUR": "€", "USD": "$", "GBP": "£", "AUD": "A$", "CAD": "C$", "CHF": "CHF", "CNY": "¥", "INR": "₹"}

def print_header():
    print("=" * 68)
    print(f"{'Welcome to Currency Converter':^70}")
    print("=" * 68)

def print_available_currencies():
    print(f"{'Available Currencies':^70}")
    currencies = list(exchange_rates.keys())
    print(" ╔═════════════════════════════════════════════════════════════════╗")
    print(" ║", end="")
    for currency in currencies:
        print(f" {currency} ", end="║")
    print("\n ╚═════════════════════════════════════════════════════════════════╝")

def currency_converter():
    print_header()  # Initial welcome message
    print_available_currencies()  # Display available currencies

    while True:
        try:
            print("====================================================================")
            baseCountry = input("\nEnter Base Currency: ").upper()
            if baseCountry not in exchange_rates:
                raise ValueError("Invalid base currency. Please choose from PHP/WON/YEN/EUR/USD/GBP/AUD/CAD/CHF/CNY/INR.")
            
            baseCurrency = input("Enter Amount: ")
            if not baseCurrency.replace('.', '', 1).isdigit():
                raise ValueError("Invalid amount. Please enter a numeric value.")
            baseCurrency = float(baseCurrency)
            
            convertCurrency = input("Enter the currency you want to convert to: ").upper()
            if convertCurrency not in exchange_rates[baseCountry]:
                raise ValueError(f"Conversion to {convertCurrency} not supported from {baseCountry}.")
            
            exchange_rate = exchange_rates[baseCountry][convertCurrency]
            result = baseCurrency * exchange_rate

            base_symbol = currency_symbols.get(baseCountry, baseCountry)
            convert_symbol = currency_symbols.get(convertCurrency, convertCurrency)

            print("-" * 68)
            if baseCountry == convertCurrency:
                print(f"Your amount remains the same: {base_symbol}{baseCurrency:.2f}")
            else:
                print(f"\t\t{base_symbol}{baseCurrency:.2f} {baseCountry} to {convertCurrency}: {convert_symbol} {result:.2f}")
            print("-" * 68)

            try_again = input("Do you want to try again? (Y/N): ").strip().lower()
            if try_again not in ['yes', 'y']:
                print("=" * 68)
                print(f"{'Thank you for using currency converter!':^68}")
                break

        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyboardInterrupt:
            print("\nOperation interrupted. Exiting...")
            break

if __name__ == "__main__":
    currency_converter()