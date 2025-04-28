import json
import os
from config import *
from fetch_flights import fetch_flight_price
from notifier import send_email, send_discord_alert

def load_previous_prices(file_path="prices.json"):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

def save_current_prices(prices, file_path="prices.json"):
    with open(file_path, "w") as f:
        json.dump(prices, f)

def main():
    previous_prices = load_previous_prices()
    current_prices = {}

    for route in ROUTES:
        key = f"{route['origin']}-{route['destination']}-{route['departure_date']}"
        try:
            current_price = fetch_flight_price(route['origin'], route['destination'], route['departure_date'])
            if current_price is None:
                print(f"No flights found for {key}")
                continue

            current_prices[key] = current_price

            old_price = previous_prices.get(key)
            if old_price:
                drop_percent = ((old_price - current_price) / old_price) * 100
                if drop_percent >= ALERT_PRICE_DROP_PERCENT or current_price <= MINIMUM_PRICE_TO_ALERT:
                    message = (f"\U0001F6A8 Price Drop Alert!\n"
                               f"Route: {key}\n"
                               f"Old Price: ${old_price}\n"
                               f"New Price: ${current_price}\n"
                               f"Drop: {drop_percent:.2f}%")
                    send_email("Flight Deal Alert", message, TO_EMAIL, SMTP_USERNAME, SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD)
                    send_discord_alert(message, DISCORD_WEBHOOK_URL)
            else:
                print(f"Tracking new route: {key} at ${current_price}")

        except Exception as e:
            print(f"Error tracking {key}: {e}")

    save_current_prices(current_prices)

if __name__ == "__main__":
    main()
