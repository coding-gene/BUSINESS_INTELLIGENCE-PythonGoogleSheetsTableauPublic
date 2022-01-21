import requests
import pandas as pd

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 200)


class CovidData:

    def __init__(self):
        self.url = 'https://www.koronavirus.hr/json/?action=podaci'

    def get_data(self):
        response = requests.get(self.url)
        df = pd.DataFrame(response.json())
        return df
