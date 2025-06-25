import functools
import traceback

from .loger_config import setup_logger

logger = setup_logger("decorators")


def log_and_handle_errors(message: str = "Error occurred"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (KeyError, ValueError) as e:
                logger.error(f"{message}: {str(e)}")
                logger.debug(traceback.format_exc())
                raise
            except Exception as e:
                logger.error(f"{message}: {str(e)}")
                logger.debug(traceback.format_exc())
                raise
        return wrapper
    return decorator
