import requests

def fetch_flight_price(origin, destination, departure_date):
    url = (
        "https://api.skypicker.com/flights"
        f"?flyFrom={origin}&to={destination}"
        f"&dateFrom={departure_date}&dateTo={departure_date}"
        f"&partner=picky&curr=USD&limit=1&sort=price&one_for_city=1"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json().get("data", [])
    if not data:
        return None
    return data[0]["price"]