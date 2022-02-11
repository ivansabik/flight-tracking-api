import requests
from aws_lambda_powertools import Logger

logger = Logger(service="gru_handler")


def handler(event=None, context=None):
    query = "procura=&terminal=&tipo=Partida&pagina=0"
    url = f"https://www.gru.com.br/en/_layouts/15/WebSiteWebParts/WebServiceCustom.asmx/GetVoos?{query}"
    response = requests.get(url)
    response.raise_for_status()
    response_dict = response.json()
    for flight in response_dict:
        # TODO remove </string> and parse as JSON
        logger.info(flight)


if __name__ == "__main__":
    handler()
