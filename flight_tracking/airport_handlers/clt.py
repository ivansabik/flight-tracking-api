import datetime

import requests
from aws_lambda_powertools import Logger

logger = Logger(service="clt_handler")


def handler(event=None, context=None):
    headers = {"api-key": "d167f645ba674f83a6f54289b524fae0", "api-version": "101"}
    utc_now = datetime.datetime.utcnow()
    first_hour_today = datetime.datetime.combine(utc_now, datetime.time(0, 0, 0, 0))
    start_epoch = first_hour_today.strftime("%s")
    end_epoch = utc_now.strftime("%s")
    url = f"https://api.cltairport.mobi/flights?scheduledTimestamp={start_epoch}..{end_epoch}"
    logger.info(
        "Requesting data",
        extra={"url": url, "start_date": first_hour_today, "end_date": utc_now},
    )
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["data"]["flights"]:
        logger.info(flight)


if __name__ == "__main__":
    handler()
