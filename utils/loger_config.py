"""
logger_config.py

This module provides a reusable function to configure and retrieve a logger instance
with a standardized format and console output. It avoids adding duplicate handlers
to prevent repeated log messages during multiple imports.

Now enhanced with colorama support for colored log levels and a blank line after each log.
"""

import logging

from colorama import Fore, Style, init

# Initialize colorama (for Windows compatibility)
init(autoreset=True)


class ColorFormatter(logging.Formatter):
    """
    Custom formatter to add colors to log levels and a blank line after each log record.
    """

    LEVEL_COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        color = self.LEVEL_COLORS.get(record.levelno, "")
        record.levelname = f"{color}{record.levelname}{Style.RESET_ALL}"

        # Format the message with the original formatter
        formatted = super().format(record)

        # Add a blank line after each log message for readability
        return formatted + "\n"


def setup_logger(name: str = __name__) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent propagation to root logger
    logger.propagate = False

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = ColorFormatter(
            "%(asctime)s - %(name)s - %(levelname)s -  %(message)s"
        )
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger
