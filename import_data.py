from io import StringIO
import requests
import requests_cache
import pandas as pd


requests_cache.install_cache('treasury_cache', expire_after=3600) #Ajoute une mémorisation temporaire des données (1 heure) pour limiter les requêtes multiples

def get_data(date : str):
    date_url = date.replace("-", "")[0:6]

    csv_url = f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/{date_url}?type=daily_treasury_yield_curve&field_tdr_date_value_month={date_url}&_format=csv"

    response = requests.get(csv_url)

    if response.status_code == 200 :
        csv_data = response.text

        if csv_data == "":
            return pd.DataFrame()

        df = pd.read_csv(StringIO(csv_data))
        return df
    
    else :
        return pd.DataFrame()
