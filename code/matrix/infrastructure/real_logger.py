import logging
import os

from matrix.infrastructure.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        os.makedirs('logs', exist_ok=True)
        logging.basicConfig(filename='logs/matrix.log', level=logging.INFO)

    def append_message_to_logs_list(self, message):
        self.logs_list.append(message)
        logging.info(message)
