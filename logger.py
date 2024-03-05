import logging


class Logger:
    _level = logging.DEBUG
    _format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
    logging.basicConfig(format=_format, level=_level)
    _logger = logging.getLogger(__name__)

    @classmethod
    @property
    def logger(cls):
        return cls._logger
