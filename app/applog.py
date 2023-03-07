import logging

logging.basicConfig(filename="log/application.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S')


def error(message):
    print(message)
    logging.error(message)

def info(message):
    print(message)
    logging.info(message)

def debug(message):
    print(message)
    logging.debug(message)

def warning(message):
    print(message)
    logging.warning(message)