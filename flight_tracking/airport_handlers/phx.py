import requests
from aws_lambda_powertools import Logger

logger = Logger(service="phx_handler")


def handler(event=None, context=None):
    url = "https://apps.skyharbor.com/flightinformation"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict:
        logger.info(flight)


if __name__ == "__main__":
    handler()
