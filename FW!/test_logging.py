import logging


def test_logdemo():
    logger = logging.getLogger(__name__)

    file = logging.FileHandler("file.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file.setFormatter(formatter)

    logger.addHandler(file)
    logger.setLevel(logging.INFO)

    logger.debug("This is debug info")
    logger.info("This is information")
    logger.error("This is Error")
    logger.critical("THis is critical")