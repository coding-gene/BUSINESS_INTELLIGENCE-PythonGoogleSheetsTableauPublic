from data.covid import CovidData
from gsapi.google import GoogleAuthentication
import logging
import pandas as pd


logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

# noinspection PyBroadException
try:
    cData = CovidData()
    gApi = GoogleAuthentication()

    df = cData.get_data()
    gApi.send_df_to_gsheets(df)
except Exception:
    logging.exception('t')
