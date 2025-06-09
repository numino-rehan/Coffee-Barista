import functools
from .loger_config import setup_logger

logger = setup_logger("decorators")


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Started: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished: {func.__name__}")
        return result
    return wrapper
