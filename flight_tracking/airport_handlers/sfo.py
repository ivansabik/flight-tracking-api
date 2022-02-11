import datetime

import requests
from aws_lambda_powertools import Logger

logger = Logger(service="sfo_handler")


def handler(event=None, context=None):
    epoch = datetime.datetime.utcnow().strftime("%s") 
    url = f"https://www.flysfo.com/api/flights-sortable/full/json?_={epoch}"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["aaData"]:
        logger.info(flight)


if __name__ == "__main__":
    handler()
