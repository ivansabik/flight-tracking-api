import requests
from aws_lambda_powertools import Logger

logger = Logger(service="fra_handler")


def handler(event=None, context=None):
    url = "https://www.frankfurt-airport.com/en/_jcr_content.flights.json/filter?perpage=1000&lang=en-GB&page=1&time=&flighttype=arrivals"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["data"]:
        logger.info(flight)
    print(len(response_dict["data"]))


if __name__ == "__main__":
    handler()
