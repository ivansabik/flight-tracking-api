import requests
from aws_lambda_powertools import Logger

logger = Logger(service="ist_handler")


def handler(event=None, context=None):
    url = "https://www.istairport.com/_layouts/15/Flights/filter-flights.aspx?{%27direction%27:%27ARRIVAL%27,%27lang%27:%27en%27,%27key%27:null,%27city%27:null,%27flight%27:null,%27type%27:null,%27page%27:1}"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["items"]:
        logger.info(flight)


if __name__ == "__main__":
    handler()
