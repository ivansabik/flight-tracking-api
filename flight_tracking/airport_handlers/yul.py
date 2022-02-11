import requests
from aws_lambda_powertools import Logger

logger = Logger(service="yul_handler")


def handler(event=None, context=None):
    url = "https://www.admtl.com/en/admtldata/api/flight?type=departure&sort=field_planned&direction=ASC&rule=24h"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["data"]:
        logger.info(flight)


if __name__ == "__main__":
    handler()
