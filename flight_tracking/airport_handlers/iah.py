import requests
from aws_lambda_powertools import Logger

logger = Logger(service="iah_handler")


def handler(event=None, context=None):
    url = "https://3rsgqsuqd1.execute-api.us-east-1.amazonaws.com/dev/flight_data?airport=iah"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict:
        logger.info(flight)


if __name__ == "__main__":
    handler()
