import requests

def ticker_to_name(ticker):
    endpoint = "https://api.coingecko.com/api/v3/coins"
    lower_coin = ticker.lower()
    name = ""

    response = requests.get(endpoint)
    data = response.json()

    for coin in data:
        if coin["symbol"] == lower_coin:
            name = coin["id"]
            break

    return name


def format_number(number):
    if number < 0:
        number = abs(number)
        if number >= 1e12:
            return "-{:,.0f}T".format(number / 1e12)
        elif number >= 1e9:
            return "-{:,.0f}B".format(number / 1e9)
        elif number >= 1e6:
            return "-{:,.0f}M".format(number / 1e6)
        else:
            return f"-{number:,.2f}"
    else:
        if number >= 1e12:
            return "{:,.0f}T".format(number / 1e12)
        elif number >= 1e9:
            return "{:,.0f}B".format(number / 1e9)
        elif number >= 1e6:
            return "{:,.0f}M".format(number / 1e6)
        else:
            return f"{number:,.2f}"

userInput = str(input(f"{45*'-'}\nEnter cryptocurrency ('done' to exit program): "))


while userInput != "done":
  
  endpoint = "https://api.coingecko.com/api/v3/simple/price"
  
  try:
    coin_id = f"{userInput.lower()}"
    response = requests.get(f"{endpoint}?ids={coin_id.lower()}&vs_currencies=usd")
  
    priceData = response.json()
    price = priceData[coin_id]["usd"]
    priceFormatted = format_number(price)
    print(f"{45*'-'}\nThe price of {coin_id.capitalize()} is ${priceFormatted}")
      
  except:
    coin_id = ticker_to_name(userInput)
    response = requests.get(f"{endpoint}?ids={coin_id.lower()}&vs_currencies=usd")
  
    priceData = response.json()
    price = priceData[coin_id]["usd"]
    priceFormatted = format_number(price)
    print(f"{45*'-'}\nThe current price of {coin_id.capitalize()} is ${priceFormatted}")
      
  userInput = str(input(f"{45*'-'}\nEnter cryptocurrency ('done' to exit program): "))

print(f"{45*'-'}\nProgram has been exited\n{45*'-'}")

  
  





