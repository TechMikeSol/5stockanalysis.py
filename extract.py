from config import key
import requests
import time 
import csv

stocks = ["AAPL", "DIS", "GOOG", "MSFT", "VOO"]


for stock in stocks:
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
    data = requests.get(url)
    json_data = data.json()
    results = json_data['results']
    stock_data = []
    print(data)
    
   
    

    for day in results:
            closing_price = day["c"]
            time_price = day["t"]
            # Convert to human readable time
            real_time = time.strftime('%Y-%m-%d', time.localtime(time_price/1000))
                
            # Create dictionary of date & price
            stock_dictionary = {
                        'Date':real_time,
                        'Closing_price':closing_price
                    }

                    # Append dictionary to stock data
            stock_data.append(stock_dictionary)
        

    with open(f"{stock}.csv", "w", newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["Date","Closing_price"])
            writer.writeheader()
            writer.writerows(stock_data)
            print(stock_data)