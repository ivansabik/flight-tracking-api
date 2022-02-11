import requests
from aws_lambda_powertools import Logger

logger = Logger(service="dxb_handler")


def handler(event=None, context=None):
    url = "https://www.dubaiairports.ae/FIDS_Cache/arrivals_summary_dxb.json"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["flights"]:
        logger.info(flight)


if __name__ == "__main__":
    handler()
