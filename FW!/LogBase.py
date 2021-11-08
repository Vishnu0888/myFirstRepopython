import inspect
import logging


class TestLogBase:

    def get_log(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        file = logging.FileHandler("file.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file.setFormatter(formatter)

        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
