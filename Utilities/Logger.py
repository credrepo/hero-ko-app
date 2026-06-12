import inspect
import logging
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
log_file_path = base_dir / "Report" / "test_log.log"


class LoggerClass:

    @staticmethod
    def log_details():

        file_handler = logging.FileHandler(log_file_path)

        log_format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s --> %(message)s"
        )

        file_handler.setFormatter(log_format)

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        if not logger.handlers:
            logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)

        return logger