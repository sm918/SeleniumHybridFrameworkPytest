import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.log",
                            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m-%d-%Y %H:%M:%S'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger