import datetime

import requests
from aws_lambda_powertools import Logger

logger = Logger(service="svo_handler")


def handler(event=None, context=None):
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    query = f"dateStart={today}T00:00:00%2B03:00&dateEnd={today}T23:59:59%2B03:00"
    url = f"https://www.svo.aero/bitrix/timetable/?direction=arrival&{query}&perPage=99999&page=0&locale=en"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["items"]:
        logger.info(flight)


if __name__ == "__main__":
    handler()
