import logging

class LOGGER :
    def __init__(self):
        # 로깅 세팅
        LOG_FORMAT = "[%(asctime)-10s] (줄 번호: %(lineno)d) %(name)s:%(levelname)s - %(message)s"
        logging.basicConfig(format=LOG_FORMAT)
        self.logger = logging.getLogger("setting")
        self.logger.setLevel(logging.DEBUG)
