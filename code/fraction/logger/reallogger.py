import logging
import os

from fraction.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        try:
            os.makedirs('tmp')
        except FileExistsError:
            pass
        logging.basicConfig(filename='tmp/myapp.log', level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
