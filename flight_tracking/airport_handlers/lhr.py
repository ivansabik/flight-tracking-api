import datetime

import requests
from aws_lambda_powertools import Logger

logger = Logger(service="lhr_handler")


def handler(event=None, context=None):
    query = datetime.datetime.today().strftime("%Y-%m-%d")
    url = f"https://api-dp-prod.dp.heathrow.com/pihub/flights/arrivals?date={query}&orderBy=localArrivalTime&excludeCodeShares=true"
    headers = {"origin": "https://www.heathrow.com"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict:
        logger.info(flight)


if __name__ == "__main__":
    handler()
