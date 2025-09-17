from logtail import LogtailHandler
import logging

SOURCE_TOKEN = 'HYN9JcsRs7e4KAFL4ms7XitL'
HOST = "s1516027.eu-nbg-2.betterstackdata.com"


def get_logger():
    handler = LogtailHandler(
        source_token=SOURCE_TOKEN,
        host=f'https://{HOST}',
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []
    logger.addHandler(handler)
    return logger


logger = get_logger()

