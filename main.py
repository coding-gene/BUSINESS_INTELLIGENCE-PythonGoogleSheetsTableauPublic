from data.covid import CovidData
from gsapi.google import Authentication
import logging


logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

# noinspection PyBroadException
try:
    cData = CovidData()
    gApi = Authentication()

    gApi.send_df_to_gsheets()
    #  print(cData.get_data())
except Exception:
    logging.exception('t')
