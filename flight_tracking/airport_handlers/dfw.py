import requests
from aws_lambda_powertools import Logger

logger = Logger(service="dfw_handler")


def handler(event=None, context=None):
    headers = {"Api-Version": "130"}
    url = f"https://api.dfwairport.mobi/flights/get"
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["data"]["flight_list"]:
        logger.info(flight)


if __name__ == "__main__":
    handler()
