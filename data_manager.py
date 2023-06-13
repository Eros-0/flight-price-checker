import requests

#Enter custom sheepy api
SHEEPY_SHEET = ""


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEEPY_SHEET)
        data = response.json()

        self.destination_data = data['prices']

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEEPY_SHEET}/{city['id']}", json=new_data)
            print(response.text)
