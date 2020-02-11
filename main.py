import coinbase
import logging
import os

APP_ENV = os.getenv("APP_ENV", "development")

def config_logging():
    log_file = "logs/production.log"
    log_level = logging.INFO

    if APP_ENV == "development":
        log_file = "logs/development.log"
        log_level = logging.DEBUG

    logging.basicConfig(filename=log_file,level=log_level)

if __name__ == "__main__":
    config_logging()

    try:
        c = coinbase.Client()
        resp = c.get_currencies()
        print(resp.text)
    except Exception as err:
        logging.error(f'{err}')
