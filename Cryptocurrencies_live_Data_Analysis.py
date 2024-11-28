import requests

# Set headers with your CoinMarketCap API key
header = {
    'X-CMC_PRO_API_KEY': '5d8c45a0-d88f-4785-a228-9650bf0910e2',  # Replace with your API key
    'Accept': 'application/json'
}

# Define the parameters for the request
params = {
    'start': '1',   
    'limit': '50',   
    'convert': 'USD' 
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

response = requests.get(url, params=params, headers=header)
json_data = response.json()

coins = json_data['data']

# Analysis 1: Identify the top 5 cryptocurrencies by market cap
top_5_by_market_cap = sorted(coins, key=lambda x: x['quote']['USD']['market_cap'], reverse=True)[:5]

print("Top 5 Cryptocurrencies by Market Cap:")
for coin in top_5_by_market_cap:
    name = coin['name']
    symbol = coin['symbol']
    market_cap = coin['quote']['USD']['market_cap']
    print(f"{name} ({symbol}) - Market Cap: ${market_cap:,.2f}")
print('-' * 40)

# Analysis 2: Calculate the average price of the top 50 cryptocurrencies
total_price = sum(coin['quote']['USD']['price'] for coin in coins)
average_price = total_price / len(coins)

print(f"Average Price of the Top 50 Cryptocurrencies: ${average_price:,.2f}")
print('-' * 40)

# Analysis 3: Analyze the highest and lowest 24-hour percentage price change
highest_change = max(coins, key=lambda x: x['quote']['USD']['percent_change_24h'])
lowest_change = min(coins, key=lambda x: x['quote']['USD']['percent_change_24h'])

print(f"Highest 24-hour Price Change: {highest_change['name']} ({highest_change['symbol']}) - {highest_change['quote']['USD']['percent_change_24h']}%")
print(f"Lowest 24-hour Price Change: {lowest_change['name']} ({lowest_change['symbol']}) - {lowest_change['quote']['USD']['percent_change_24h']}%")
