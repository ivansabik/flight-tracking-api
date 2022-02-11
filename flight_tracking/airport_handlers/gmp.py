import requests
from aws_lambda_powertools import Logger

logger = Logger(service="gmp_handler")


def handler(event=None, context=None):
    query = "pInoutGbn=O&pAirport=GMP&pSthourMin=0%3A00&pEnhourMin=23%3A59&pAirline=&pGbn=&pAirlinenum="
    url = f"https://www.airport.co.kr/gimpoeng/ajaxf/frPryInfoSvc/getPryInfoList.do?{query}"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict["data"]:
        logger.info(flight)


if __name__ == "__main__":
    handler()
