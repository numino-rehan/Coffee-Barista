import logging

# Set up the basic configuration for logging to output to the console
#logging.basicConfig(level=logging.INFO)  # Logs with level INFO and above
logger = logging.getLogger()

def log_and_print(msg, level='INFO'):
    if level == 'INFO':
        logger.info(msg)
    elif level == 'WARNING':
        logger.warning(msg)
    elif level == 'ERROR':
        logger.error(msg)
    else:
        print(f"Unknown level: {level}")

    print(msg)




