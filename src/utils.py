import logging


def println(msg: str):
    print(msg + "\n", end="", flush=True)


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    return logger
